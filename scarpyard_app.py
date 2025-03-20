from flask import Flask, render_template, request
import mysqlDB_connector
#import snowflake_connector
sracpyard_app = Flask(__name__)

#Connection setup with my-sql db
sqldb_cur = mysqlDB_connector.create_connections()


#page routing start
@sracpyard_app.route('/')
def order_submit():
    return render_template('order_submit.html')



if __name__=='__main__':
    sracpyard_app.run(debug=True)