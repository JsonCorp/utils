import os

def split_file(original_file, chunk_size_mb):
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    with open(original_file, 'rb') as f:
        file_size = os.path.getsize(original_file)
        num_chunks = (file_size + chunk_size_bytes - 1) // chunk_size_bytes
        folder_name = os.path.splitext(original_file)[0]
        os.makedirs(folder_name, exist_ok=True)
        filename, file_extension = os.path.splitext(original_file)
        for i in range(num_chunks):
            chunk_start = i * chunk_size_bytes
            chunk_end = min((i + 1) * chunk_size_bytes, file_size)
            chunk = f.read(chunk_end - chunk_start)
            with open(os.path.join(folder_name, f"{filename}_{i}{file_extension}"), 'wb') as chunk_file:
                chunk_file.write(chunk)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python split_file.py <original_file> <chunk_size_mb>")
        sys.exit(1)
    original_file = sys.argv[1]
    chunk_size_mb = int(sys.argv[2])
    split_file(original_file, chunk_size_mb)