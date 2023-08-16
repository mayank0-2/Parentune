from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/parentune?unix_socket=/opt/lampp/var/mysql/mysql.sock'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def data () :
    if request.method == 'GET':
        query = f"SELECT plus_pre_schoolss.school_name ,plus_pre_schoolss.address, plus_pre_schoolss.city, plus_pre_schools_detail.contact_number, plus_pre_schools_detail.website, plus_pre_schools_detail.map_url FROM plus_pre_schoolss INNER JOIN plus_pre_schools_detail on plus_pre_schoolss.id = plus_pre_schools_detail.schoolID WHERE plus_pre_schools_detail.schoolId"
        data = [dict(row) for row in mysql.engine.execute(query).fetchall()]
        return {"data" : data}
    
    
    
if __name__ == "__main__":
    app.run(debug=True)

