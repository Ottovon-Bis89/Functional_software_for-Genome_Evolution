
import os

def process_files_in_directory(directory):
    """Process all valid chromosome files in the specified directory."""
    for filename in os.listdir(directory):
        if is_valid_file(filename):
            chromosome_number = extract_chromosome_number(filename)
            process_file(directory, filename, chromosome_number)


def is_valid_file(filename):
    """Check if the filename starts with 'chr' and ends with '_recomb.txt'."""
    return filename.startswith('chr') and filename.endswith('_recomb.txt') # change names of chromosomes as you like


def extract_chromosome_number(filename):
    """Extract the chromosome number from the filename."""
    return filename.split('_')[0][3:]


def process_file(directory, filename, chromosome_number):
    """Process a single file and write the output to a BED file."""
    input_filepath = os.path.join(directory, filename)
    output_filepath = f"chr{chromosome_number}_output.bed"
    
    with open(input_filepath, "r") as in_f, open(output_filepath, "w") as out_f:
        write_bed_headers(out_f)
        write_bed_content(in_f, out_f, chromosome_number)


def write_bed_headers(out_f):
    """Write the column headers to the BED file."""
    out_f.write("chr\tstart\tstop\n")


def write_bed_content(in_f, out_f, chromosome_number):
    """Write the content of the BED file by processing input data."""
    for line in in_f:
        start = int(line.strip())
        stop = calculate_stop_position(start)
        out_f.write(f"{chromosome_number}\t{start}\t{stop}\n")


def calculate_stop_position(start):
    """Calculate the stop position from the start position."""
    return start + 1


if __name__ == "__main__":
    directory = "directory to chromosome files"
    process_files_in_directory(directory)


