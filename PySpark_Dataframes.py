# from pyspark import SparkContext, SparkConf
# from pyspark.sql import SQLContext
# from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

# # Lets see SparkContext in a little bit more detail :--
# conf = SparkConf().setMaster('local')
# sc = SparkContext(conf=conf)
# sc2 = SparkContext(conf=conf)
# sql = SQLContext(sc)

# # lets see the SparkContext object
# print(">> SparkContext Object 1  : ",sc)
# print(">> SparkContext Object 2  : ",sc2) # can be solved by setting spark.driver.allowMultipleContexts to 'true'
# # print(">> SQLContext Object      : ",sql)
# print(">> StreamingContext Object: ",stream)
# print("SparkContext Object: ",sc2)


#-----------------------------------------------------------------------------------------------
'''
What is SparkSession?
SparkSession = SparkContext + SQLContext + HiveContext + StreamingContext
SparkSession can be created from an existing SparkContext using SQLContext
'''
#-----------------------------------------------------------------------------------------------
# ss = sql.sparkSession # From PREVIOUS SPARKCONTEXT
# ss = SparkSession.builder.appName('Intellipaat-Dataframes').master('local').getOrCreate()
# ss2 = ss.newSession()
# ss3 = ss.newSession()

# print("1st SparkSession: ",ss)
# print("2nd SparkSession: ",ss2)
# print("3rd SparkSession: ",ss3)
# print("SparkContext of ss {} ".format(ss.sparkContext))
# print("SparkContext of ss {} ".format(ss2.sparkContext))
# print("SparkContext of ss {} ".format(ss3.sparkContext))


#-----------------------------------------------------------------------------------------------
'''
Reading/Writing from/to Data Sources 
CSV     > ss.read.format('csv').option().option().schema(<schema-name>).load(<file>)
          ss.write.format('csv').mode(<write-mode-options>).option().option().save(<file>)
           
Parquet > ss.read.format('parquet').option().option().load(<file>) # SCHEMA IS NOT NEEDED
          ss.write.format('parquet').option().mode(<write-mode-options>).save(<file>)
          
JSON    > ss.read.format('json').option().option().schema(<schema-name>).load(<file>)
          ss.write.format('json').option().mode(<write-mode-options>).save(<file>)
          
ORC     > ss.read.format('orc').option().option().load(<file>) # SCHEMA IS NOT NEEDED
          ss.write.format('orc').option().mode(<write-mode-options>).save(<file>)
          
write modes = "append" | "overwrite" | "errorIfExists" | "ignore"

** Data can be read from JDBC sources too.
'''
#-----------------------------------------------------------------------------------------------
ss = SparkSession.builder.appName('intellipaat-sparksession').master('local').getOrCreate()
# input_file_csv = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data_ORIG.csv'
# input_file_csv = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data_wo_header.csv'
# df1 = ss.read.format('csv').option('header','true').load(input_file_csv)
# df1.show()

# input_file_parquet = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/covid-19_patients_data.parquet/part-00000-cffc2fa1-1dd0-4b68-8005-e08f9806ee19-c000.snappy.parquet'
# df1 = ss.read.format('parquet').load(input_file_parquet) # No need to provide any schema
# df1.printSchema()
# df1.show()

# input_file_json = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/car_sales_information.json'
# input_file_json = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/restaurants.json'
# df1 = ss.read.format('json').option('inferSchema','true').load(input_file_json)
# df1.show()
# df1.printSchema()

# df1 = sql.read.format('json').option('inferSchema','true').load(input_file_json)
# df1.show()

# df1 = ss.read.format('json').option('inferSchema','true').load(input_file_json)
# df1.printSchema()

#-----------------------------------------------------------------------------------------------
'''
Spark Data Types (has to be imported from pyspark.sql.types)
- ByteType() > 1byte 
- ShortType() > 2bytes
- IntegerType()
- LongType() > 8bytes
- FloatType(), DecimalType()
- StringType()
- BinaryType(), BooleanType()
- TimestampType() > Python type datetime.datetime
- DateType() > Python type datetime.date
- ArrayType(<elementType>) > list, tuple (elementType should be from above list)
- MapType(<keyType>,<valueType>) > Python dictionary
- StructType() > To define the entire schema
- StructField() > To define individual fields  

Structure to define schema:
StructType([ StructField(), StructField(), StructField() ])

To check the schema use printSchema().
'''
#-----------------------------------------------------------------------------------------------
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType, FloatType


# input_restaurant_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/restaurants.json'
# input_emp_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data_ORIG.csv'

# emp_schema = StructType(
#     [
#         StructField('dept_id', IntegerType(), True),
#         StructField('first_name', StringType(), True),
#         StructField('last_name', StringType(), True),
#         StructField('email', StringType(), True),
#         StructField('role', StringType(), True)
#     ]
# )
#
# empDf = ss.read.format('csv').schema(emp_schema).load((input_emp_file))
# empDf.printSchema()
# empDf.show()

# restaurant_schema = StructType(
#     [
#         StructField("address",StructType([StructField("building",StringType(),True),
#                                           StructField("coord",ArrayType(FloatType()),True),
#                                           StructField("street",StringType(),True),
#                                           StructField("zipcode",StringType(),True)]),
#                      True),
#         StructField("borough",StringType(),False),
#         StructField("cuisine",StringType(),False),
#         StructField("grades",ArrayType(StructType([StructField("date",StructType([StructField("$date",IntegerType(),False)]),False),
#                                                    StructField("grade",StringType(),False),
#                                                    StructField("score",IntegerType(),False)]))
#                      ,False),
#         StructField("name",StringType(),False),
#         StructField("restaurant_id",IntegerType(),False)
#     ]
# )

# df1 = ss.read.format('json').schema(restaurant_schema).load(input_restaurant_file)
# df1 = ss.read.format('json').option('inferSchema','true').load(input_restaurant_file)
# df1 = ss.read.format('json').load(input_restaurant_file).schem(schema) # Will give error
# df1.printSchema()
# df1.show()



#-----------------------------------------------------------------------------------------------
'''
Convert RDD to Dataframe
- createDataFrame(<rdd>,schema=<myschema>)
  1. Create an RDD
  2. Convert it to type Row, Tuple, List etc.
  3. Define schema
  3. Apply createDataFrame method on the RDD created in step 2.
  Note: RDD need to have type Row, Tuple, List, Int, Boolean, Pandas DataFrame. If RDD is 
        created from CSV/JSON files then it has to be transformed to contain new RDD with
        above data types. Then the new RDD can be converted to a DataFrame.
          
- toDF(<list_of_column_names>) 
  Note: RDD has to be passed with type Row, Tuple, List, Int, Boolean, just the way it is
        done with 'createDataFrame'. The column names have to be passed as a LIST in the 
        argument of toDF. If we do not pass List of column names then the column names would 
        be numbered as _1, _2, _3 and so on.
        
- From an existing SparkContext using SQLContext
  df = sql.read.format('')...
'''
#-----------------------------------------------------------------------------------------------
from pyspark.sql.types import StringType, StructField, StructType, IntegerType
# input_file_csv = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data.csv'

# # from pyspark import SparkContext, SparkConf
# # conf = SparkConf().setMaster('local')
# # sc = SparkContext(conf=conf)
# sc = ss.sparkContext
#
# schema = StructType(
#     [
#         StructField("dept_id", IntegerType(), False),
#         StructField("first_name", StringType(), False),
#         StructField("last_name", StringType(), False),
#         StructField("email", StringType(), False),
#         StructField("role", StringType(), False),
#     ]
# )
#
# def convert_to_list(x):
#     x = x.split(',')
#     # return int(x[0]),x[1],x[2],x[3],x[4]
#     return int(x[0]),x[1],x[2],x[3],x[4]
#
# inputRdd1 = sc.textFile(input_file_csv)
# inputRdd2 = inputRdd1.map(lambda x: convert_to_list(x))
# inputDf = ss.createDataFrame(inputRdd2,schema=schema)

# inputDf2 = inputRdd2.toDF(["dept_id","first_name","last_name","email","role"])
# inputDf2.show()


#-----------------------------------------------------------------------------------------------
# col, column function
# Note: Please install pyspark-stubs to use col and column functions. This is needed for PyCharm
#       IDE as these functions are resolved at runtime.
#-----------------------------------------------------------------------------------------------
from pyspark.sql.functions import col, column

# input_jpmc_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/JPMC_Bank_Database.csv'
# ss = SparkSession.builder.getOrCreate()

# df1 = ss.read.format('csv').option('header','true').load(input_jpmc_file)
# df1.show()
# print(df1.columns)
# df1.printSchema()

# df1.select(col("Branch_Name").startswith("J"))
# df1.select("Branch_Name","2010_Deposits").filter(col("2010_Deposits").cast(IntegerType()) > 1000000).show(5)

# df2 = df1.select("Branch_Name","2010_Deposits")
# df2.show()
# df1.select("Branch_Name","Established_Date").filter(df1["Branch_Name"].startswith("JP")).show()


#-----------------------------------------------------------------------------------------------
'''
DataFrame Transformations
- select
- limit
- filter | where
- orderBy
- sort
- groupBy
- union
- join
- agg
'''
#-----------------------------------------------------------------------------------------------
# input_jpmc_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/JPMC_Bank_Database.csv'
# df1 = ss.read.format('csv').option('header','true').load(input_jpmc_file)

# df1.printSchema()

# SELECT
# df1.select('Institution_Name','Branch_Name','Established_Date').show()
# df1.select('Institution_Name','Branch_Name','Established_Date').limit(10).show()

# FILTER | WHERE
#----------------
# df2 = df1.select('Institution_Name','Branch_Name','Established_Date')
# df3 = df2.filter(col("Branch_Name").startswith("J"))
# df3 = df2.where(col("Branch_Name").startswith("J"))
# df3.show()
# print(df3.count())

# ORDERBY | SORT | LIMIT
#------------------------
# df2 = df1.select("Branch_Name", "2010_Deposits","Established_Date")
# df3 = df2.orderBy(col("2010_Deposits").cast(IntegerType()).desc())
# df3 = df2.sort(col("2010_Deposits").cast(IntegerType()).desc())
# df4 = df3.limit(5)
# df4.show()
# df2 = df1.select('Branch_Name').distinct().limit(5)
# df2 = df1.select('Branch_Name').orderBy('Branch_Name')
# df2.show()

#---------------------------------------------------------------------------------------------------------
# JOIN - Joins with another DataFrame
# join(DataFrame, <list of col names | single col | a join expression>,
#                 <'inner|cross|left_outer|right_outer'>)
#---------------------------------------------------------------------------------------------------------
# emp_data_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data_ORIG.csv'
# dept_data_file = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/dept_data.csv'
# empDf = ss.read.format('csv').option('header','true').load(emp_data_file)
# deptDf = ss.read.format('csv').option('header','true').load(dept_data_file)

# joined_data = empDf.join(deptDf, empDf.dept_id == deptDf.dept_id, 'inner')
# emp = empDf.alias('emp')
# dept = empDf.alias('dept')
# joined_data = empDf.join(deptDf, empDf.dept_id == deptDf.dept_id, 'inner').drop(deptDf.dept_id)
# joined_data = emp.join(deptDf, ['dept_id'] , 'inner')
# joined_data2 = joined_data.select('dept_id','first_name','email','dept_name')

# What if column names are different >>>
# emp = empDf.alias('emp').withColumnRenamed('deptid','dept_id')
# joined_data = emp.join(deptDf, ['dept_id'] , 'inner')

# joined_data.show()

# join using multiple columns >>>
# inspection = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/inspections_plus.csv'
# violations = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/violations_plus.csv'

# from pyspark.sql.types import StructField, StructType
# from pyspark.sql.types import StringType, IntegerType

# inspection_schema = StructType(
#     [
#         StructField('location_id',IntegerType(),True),
#         StructField('inspection_id',IntegerType(),True),
#         StructField('inspection_date',StringType(),True),
#         StructField('description',StringType(),True),
#     ]
# )

# violations_schema = StructType(
#     [
#         StructField('location_id',IntegerType(),True),
#         StructField('violation_date',StringType(),True),
#         StructField('violation_code', IntegerType(),True),
#         StructField('violation_category', StringType(),True),
#         StructField('violation_desc',StringType(), True)
#     ]
# )

# inspectionDf = ss.read.format('csv').schema(inspection_schema).load(inspection)
# violationsDf = ss.read.format('csv').schema(violations_schema).load(violations)
# vDf = violationsDf.withColumnRenamed('violation_date','date')
# iDf = inspectionDf.withColumnRenamed('inspection_date','date')

# joined_data = inspectionDf.join(violationsDf, (inspectionDf.location_id == violationsDf.location_id) & \
#                                               (inspectionDf.inspection_date == violationsDf.violation_date),
#                                 'inner').drop('violationsDf.violation_date','violationsDf.location_id')

# joined_data = iDf.join(vDf, ['location_id','date'], 'inner')
# joined_data.show()

# LIT function
#------------------
# from pyspark.sql.functions import lit
#
# nu = 10
# chr = "Shommodeep Dey"
# dec = 24.08
#
# df = violationsDf.select(lit(nu),lit(chr),lit(dec))
# df.printSchema()
# print(df.dtypes)


#---------------------------------------------------------------------------------------------------------
# groupBy and agg - Pass the no. of columns and get aggregate value from it
# avg, count, max, mean, min, sum, countDistinct, stddev
#---------------------------------------------------------------------------------------------------------
# covid_data = '/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/covid-19_patients_data_ORIG.csv'
#
# covidDf = ss.read.format('csv').option('header','true').load(covid_data)
#
# df1 = covidDf.groupBy('gender').max()
# df1.show()

#?? QNS 1 >>> Find the top 10 product that has the highest occurance in file
#---------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------
# Handle complex structure
#---------------------------------------------------------------------------------------------------------