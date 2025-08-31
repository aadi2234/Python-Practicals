def copy_with_uppercase(input_file,output_file):
    try:
        with open(input_file,'r') as f_input:
            with open(output_file,'w') as f_output:
                for line in f_input:
                    f_output.write(line.upper())
        print("File contents copied and converted to uppercase successfully!")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An Error Occurred:",e)

input_file='input.txt'
output_file='output.txt'
copy_with_uppercase(input_file,output_file)
            