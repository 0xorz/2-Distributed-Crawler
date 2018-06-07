import sys

def split_file_into_chunks(filepath, chunks_count):
    with open(filepath, 'r') as fileobj:
        lines = fileobj.readlines()

    chunk_size = len(lines) // chunks_count

    for i in range(chunks_count):
        start = chunk_size * i
        end = chunk_size * (i + 1)
        if i == chunks_count - 1:
            end = len(lines)
        
        with open('chunks/' + str(i) + '.csv', 'a') as fileobj:
            for line in lines[start:end]:
                fileobj.write(line)

if __name__ == "__main__":
    filepath = sys.argv[1]
    chunks_count = int(sys.argv[2])

    split_file_into_chunks(filepath, chunks_count)