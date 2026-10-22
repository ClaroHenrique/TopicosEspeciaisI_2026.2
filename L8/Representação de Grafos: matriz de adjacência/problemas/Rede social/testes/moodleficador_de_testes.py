#!/usr/bin/env python3
"""Converte arquivos .in/.out em um único bloco no formato do Moodle.

Exemplo de saída:
Case=T1
Input=5
9 4 7 2 8
Output=2

Case=T2
Input=5
1 4 7 2 8
Output=1
"""

from __future__ import annotations

import argparse
from pathlib import Path


def normalize_text(path: Path) -> str:
    """Lê o arquivo e remove apenas a quebra final de linha."""
    return path.read_text(encoding="utf-8").rstrip("\n")


def find_case_files(test_dir: Path):
    """Retorna os pares (stem_num, .in, .out) ordenados por número."""
    candidates = {}

    for file in test_dir.iterdir():
        if not file.is_file():
            continue

        if file.suffix.lower() == ".in":
            candidates.setdefault(file.stem, {})["in"] = file
        elif file.suffix.lower() == ".out":
            candidates.setdefault(file.stem, {})["out"] = file

    cases = []
    for stem, files in candidates.items():
        if "in" in files and "out" in files:
            try:
                order = int(stem)
            except ValueError:
                order = stem
            cases.append((order, files["in"], files["out"]))

    cases.sort(key=lambda item: item[0])
    return cases


def build_moodle_block(test_dir: Path, output_path: Path):
    case_files = find_case_files(test_dir)
    if not case_files:
        raise FileNotFoundError(f"Nenhum par .in/.out encontrado em: {test_dir}")

    blocks = []
    for idx, (_, in_file, out_file) in enumerate(case_files, start=1):
        input_text = normalize_text(in_file)
        output_text = normalize_text(out_file)

        blocks.append(
            "\n".join(
                [
                    f"Case=T{idx}",
                    f"Input={input_text}",
                    f"Output={output_text}",
                ]
            )
        )

    content = "\n\n".join(blocks) + "\n"
    output_path.write_text(content, encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Converte arquivos .in/.out em um texto no formato do Moodle."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Diretório com os arquivos de teste (.in e .out).",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Arquivo de saída. Se não for informado, usa 'testes_moodle.txt' no mesmo diretório.",
    )
    args = parser.parse_args()

    test_dir = Path(args.directory).resolve()
    output_path = Path(args.output).resolve() if args.output else test_dir / "testes_moodle.txt"

    result = build_moodle_block(test_dir, output_path)
    print(f"Arquivo gerado em: {result}")


if __name__ == "__main__":
    main()
