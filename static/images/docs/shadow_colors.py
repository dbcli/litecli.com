import asyncio
from pathlib import Path
import sys
import subprocess

colors = [
        "transparent",
        # "268CFF",   # blue
        # "9BC53D",   # green
        # "FDE74C",   # yellow
        # "E55934",   # red
        # "FA7921",   # orange
        ]


async def convert(filename, color, output_dir, live=False):
    output_file_path = output_dir / (color + "_" + filename)
    cmd = f"convert {filename} \( +clone -background black -shadow 80x20+0+15 \) +swap -background '#{color}' -layers merge +repage {output_file_path}"
    print(cmd)
    if live:
        proc = await asyncio.create_subprocess_shell(cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
        # stdout, stderr = await proc.communicate()
        return (proc.returncode, filename, color)
    return (0, filename, color)

async def main(files):
    output_dir = "output"
    output_dir_path = Path(".") / output_dir
    if not output_dir_path.exists():
        await asyncio.create_subprocess_shell(f"mkdir {output_dir_path}")

    live = True
    for color in colors:
        results = await asyncio.gather(*[convert(f, color, output_dir=output_dir_path, live=live) for f in files])
    print("Results:", results)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"{sys.argv[0]} filenames")
    asyncio.run(main(sys.argv[1:]))
