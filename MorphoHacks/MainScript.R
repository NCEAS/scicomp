# User-dependent variables ------------------------------------------------
# Absolute path to folder containing the scripts
scripts_path <- ""
# Absolute path to your file to be processed
read_dir <- ""
# Absolute path to directory in which to write script outputs
write_dir <- ""
# A custom code used in your data to indicate any missing data. This excludes
# blank cells (represented in R as an empty character vector or string) as well
# as R's own code, "NA".
custom_code <- ""

# Non-user operations -----------------------------------------------------
# Clear environment
library(gdata)
keep(scripts_path, read_dir, write_dir, custom_code, sure = TRUE)

# Source the other script
source(file.path(scripts_path, "WriteUniqueFieldValues.R"))

# Call function with user inputs
WriteUniqueFieldValues(.read_dir = read_dir,
                       .write_dir = write_dir,
                       .missing_code = custom_code)
