{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "717ced8c-45c8-4104-b458-6eee074f4649",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total lines: 6990280, Lines per file: 699028\n",
      "✅ JSON file successfully split into smaller parts!\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "input_file = r\"C:\\Users\\mresh\\OneDrive\\Desktop\\RESH_PROJECTS\\yelp project\\yelp_dataset\\yelp_academic_dataset_review.json\"  # Your 5GB JSON file\n",
    "output_prefix = \"split_file_\"  # Prefix for output files\n",
    "num_files = 10  # Number of files to split into\n",
    "\n",
    "# Count total lines (objects) in the file\n",
    "with open(input_file, \"r\" , encoding=\"utf8\") as f:\n",
    "    total_lines = sum(1 for _ in f)  \n",
    "\n",
    "lines_per_file = total_lines // num_files  # Lines per split file\n",
    "\n",
    "print(f\"Total lines: {total_lines}, Lines per file: {lines_per_file}\")\n",
    "\n",
    "# Now split into multiple smaller files\n",
    "with open(input_file, \"r\" , encoding=\"utf8\") as f:\n",
    "    for i in range(num_files):\n",
    "        output_filename = f\"{output_prefix}{i+1}.json\"\n",
    "        \n",
    "        with open(output_filename, \"w\", encoding=\"utf8\" ) as out_file:\n",
    "            for j in range(lines_per_file):\n",
    "                line = f.readline()\n",
    "                if not line:\n",
    "                    break  # Stop if file ends early\n",
    "                out_file.write(line)\n",
    "\n",
    "print(\"✅ JSON file successfully split into smaller parts!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a68aad91-ca26-4fdc-975d-4e0255498596",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "your split files are saved here C:\\Users\\mresh\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(\"your split files are saved here\" , os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85d6bc8c-42a7-4cd8-8781-ce90e0664c95",
   "metadata": {},
   "outputs": [],
   "source": [
    "%history -f YelpReviewCode.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "352430d1-d72f-4565-9501-312f5f15e06b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
