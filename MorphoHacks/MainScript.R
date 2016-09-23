# User-dependent variables ------------------------------------------------
# Absolute path to folder containing MainScript.R and WriteUniqueFieldValues.R
scripts_path <- ""
# Absolute path to your data-file input
read_dir <- ""
# Absolute path to the directory in which to write script outputs
write_dir <- ""
# A custom string used in your data to indicate any missing data. If your
# data represents missing values by empty cells, or even R's "NA" (without the
# quotes), then do not modify this variable's value.
custom_string_for_missing_values <- ""

# Non-user operations -----------------------------------------------------
# Clear environment
library(gdata)
keep(scripts_path, read_dir, write_dir, custom_code, sure = TRUE)

# Source the other script
source(file.path(scripts_path, "WriteUniqueFieldValues.R"))

# Call function with user inputs
WriteUniqueFieldValues(.read_dir = read_dir,
                       .write_dir = write_dir,
                       .missing_code = custom_string_for_missing_values)
