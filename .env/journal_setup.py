# journal_setup.py
# Final cleanup: organises root, creates .vscode/ and .env/, compiles PDF.
import os, shutil, subprocess, sys, json

base = os.path.dirname(os.path.abspath(__file__))
os.chdir(base)

def log(msg): print(f'[setup] {msg}')

# ── 1. Create assets/papers (idempotent) ──────────────────────
os.makedirs(os.path.join(base, 'assets', 'papers'), exist_ok=True)

# ── 2. Move original paper directories (if still in root) ────
moves = [
    ('Shannon_s_Theorem_and_Polar_Codes', os.path.join('assets', 'papers', 'shannon-polar-codes')),
    ('The_Qubit_and_Shor_s_Algorithm',    os.path.join('assets', 'papers', 'qubit-shor')),
]
for src_name, dst_rel in moves:
    src = os.path.join(base, src_name)
    dst = os.path.join(base, dst_rel)
    if os.path.exists(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(src, dst)
        log(f'Moved {src_name} -> {dst_rel}')

# ── 3. Rename qubit-shor sections (idempotent) ────────────────
secs = os.path.join(base, 'assets', 'papers', 'qubit-shor', 'sections')
renames = {
    '0) preliminaries.tex':                          '00-preliminaries.tex',
    '1) Intro to cryptography.tex':                  '01-intro-cryptography.tex',
    '2)Intro to the world of quantum computing.tex': '02-quantum-computing.tex',
    '3) Shor algo.tex':                              '03-shor-algo.tex',
    '4) Final thought.tex':                          '04-final-thought.tex',
}
if os.path.isdir(secs):
    for old, new in renames.items():
        op = os.path.join(secs, old)
        np = os.path.join(secs, new)
        if os.path.exists(op):
            os.rename(op, np)
            log(f'Renamed: {new}')

# ── 4. Move HCMS.pdf to assets/ (if still in root) ───────────
for pdf_name in ('HCMS.pdf', 'HCMR.pdf'):
    src = os.path.join(base, pdf_name)
    dst = os.path.join(base, 'assets', pdf_name)
    if os.path.exists(src):
        shutil.move(src, dst)
        log(f'Moved {pdf_name} -> assets/')

# ── 5. Move article-template.tex to template/ ────────────────
tpl_src = os.path.join(base, 'article-template.tex')
tpl_dst = os.path.join(base, 'template', 'article-template.tex')
if os.path.exists(tpl_src) and not os.path.exists(tpl_dst):
    shutil.move(tpl_src, tpl_dst)
    log('Moved article-template.tex -> template/')

# ── 6. Create .env/ and move utility files there ─────────────
env_dir = os.path.join(base, '.env')
os.makedirs(env_dir, exist_ok=True)
to_env = [
    'SETUP.bat', 'install_vscode_launch.bat', 'run_script.bat',
    'run_setup.bat', 'TEMPLATE-README.md',
]
for f in to_env:
    src = os.path.join(base, f)
    dst = os.path.join(env_dir, f)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.move(src, dst)
        log(f'Moved {f} -> .env/')

# ── 7. Delete all remaining junk files from root ─────────────
junk_files = [
    'article-01-shannon.tex', 'article-02-shor.tex', 'article-03-placeholder.tex',
    'COMPILE.bat', 'create_dirs.bat', 'create_dirs.py',
    'execute_all_steps.bat', 'execute_all_steps.ps1',
    'execute_final.py', 'execute_sequence.py',
    'execute_steps.bat', 'execute_steps.py',
    'EXECUTION_REPORT.md', 'fix_structure.py',
    'reorg_temp.py', 'run_all.bat', 'run_all_steps.py',
    'run_execute_sequence.bat', 'run_steps.bat',
    'run_with_output.py', 'test_exec.py', 'wrapper.py',
    'journal-cover.tex', 'journal-editorial.tex',
]
for f in junk_files:
    fp = os.path.join(base, f)
    if os.path.exists(fp):
        os.remove(fp)
        log(f'Deleted: {f}')

# ── 8. Delete redundant subdirs inside articles/ ─────────────
for d in ('01-shannon-polar-codes', '02-qubit-shor', '03-placeholder'):
    dp = os.path.join(base, 'articles', d)
    if os.path.exists(dp):
        shutil.rmtree(dp)
        log(f'Deleted: articles/{d}/')

# ── 9. Create .vscode/ with tasks.json and launch.json ───────
vscode_dir = os.path.join(base, '.vscode')
os.makedirs(vscode_dir, exist_ok=True)

tasks = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Compile Journal PDF",
            "type": "shell",
            "command": "pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex",
            "options": {"cwd": "${workspaceFolder}"},
            "group": {"kind": "build", "isDefault": True},
            "presentation": {"reveal": "always", "panel": "shared"},
            "problemMatcher": []
        }
    ]
}
tasks_path = os.path.join(vscode_dir, 'tasks.json')
with open(tasks_path, 'w') as f:
    json.dump(tasks, f, indent=2)
log('Written: .vscode/tasks.json')

# Move launch.json from root to .vscode/ (if not already there)
launch_src = os.path.join(base, 'launch.json')
launch_dst = os.path.join(vscode_dir, 'launch.json')
if os.path.exists(launch_src) and not os.path.exists(launch_dst):
    shutil.move(launch_src, launch_dst)
    log('Moved launch.json -> .vscode/launch.json')
elif not os.path.exists(launch_dst):
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Setup & Compile Journal",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/.env/journal_setup.py",
                "console": "integratedTerminal",
                "cwd": "${workspaceFolder}"
            }
        ]
    }
    with open(launch_dst, 'w') as f:
        json.dump(launch, f, indent=2)
    log('Written: .vscode/launch.json')

# ── 10. Clean LaTeX aux files ─────────────────────────────────
aux_exts = ('.aux', '.log', '.out', '.toc', '.fls', '.fdb_latexmk', '.synctex.gz', '.bbl', '.blg')
for fname in os.listdir(base):
    if any(fname.endswith(ext) for ext in aux_exts):
        try:
            os.remove(os.path.join(base, fname))
            log(f'Cleaned: {fname}')
        except Exception as e:
            log(f'Could not clean {fname}: {e}')

log('\nRoot directory after cleanup:')
for f in sorted(os.listdir(base)):
    print(f'  {f}')

# ── 11. Compile (two passes for cross-references) ─────────────
log('\nCompiling main.tex (pass 1)...')
r1 = subprocess.run(
    ['pdflatex', '-interaction=nonstopmode', 'main.tex'],
    capture_output=True, text=True, cwd=base
)
print(r1.stdout[-3000:] if len(r1.stdout) > 3000 else r1.stdout)
if r1.returncode != 0:
    print('=== STDERR ===')
    print(r1.stderr[-2000:])
    log_path = os.path.join(base, 'main.log')
    if os.path.exists(log_path):
        with open(log_path, encoding='latin-1') as lf:
            lines = lf.readlines()
        print('=== LAST 80 LINES OF main.log ===')
        print(''.join(lines[-80:]))
    sys.exit(1)

log('\nCompiling main.tex (pass 2 for references)...')
r2 = subprocess.run(
    ['pdflatex', '-interaction=nonstopmode', 'main.tex'],
    capture_output=True, text=True, cwd=base
)
print(r2.stdout[-1000:] if len(r2.stdout) > 1000 else r2.stdout)

pdf = os.path.join(base, 'main.pdf')
if os.path.exists(pdf):
    size = os.path.getsize(pdf)
    log(f'\n=== SUCCESS: main.pdf created ({size:,} bytes) ===')
else:
    log('\n=== FAILED: main.pdf not found ===')
    sys.exit(1)

# ── 12. Move self to .env/ ────────────────────────────────────
self_dst = os.path.join(env_dir, 'journal_setup.py')
if not os.path.exists(self_dst):
    try:
        shutil.copy2(__file__, self_dst)
        os.remove(__file__)
        log(f'Moved journal_setup.py -> .env/')
    except Exception as e:
        log(f'Could not move self: {e}')

log('\nDone! Open main.pdf to view the journal.')
log('To recompile: Ctrl+Shift+B in VS Code, or run:')
log('  pdflatex main.tex && pdflatex main.tex')
