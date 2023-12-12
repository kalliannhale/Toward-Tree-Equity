# Toward-Tree-Equity

This project is limited to Boston, MA; and, in particular, has been designed only for those neighborhoods with specific canopy expansion strategies outlined in the Boston Urban Forest Plan, more of which can be : https://www.boston.gov/departments/parks-and-recreation/urban-forest-plan.

* Please format addresses accordingly: 'number name street, Boston, MA'.
* Make sure to include commas; do not include unit numbers.
* Street abbreviations such as the example,'100 Wilmer Ave, Boston, MA' are acceptable.

IMPORTANT!! PLEASE READ:

* If multiple addresses are failing the geocoding process:
  
  *** check the filepaths in the read_csv() method in the neighborhood module
  
  *** copy & paste the absolute path of the files of the same name into the associated dictionary as appropriate.

  *** proper categorization of each address relies heavily on reading the provided data set files! However the package is being run, they MUST be accessible.

  LIMITATIONS:
  * Only one tree may be entered at a time.
