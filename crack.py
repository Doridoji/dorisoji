import subprocess
import multiprocessing
import time
from tqdm import tqdm

def run_soul(_):
    subprocess.run(["python3", "soul.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    num_processes = multiprocessing.cpu_count()
    iterations_per_process = 1000000

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        with tqdm(total=1000000, desc="Running soul.py") as pbar:
            for _ in pool.imap_unordered(run_soul, range(iterations_per_process)):
                pbar.update(1)

    end_time = time.time()
    print(f"\nExecution completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
