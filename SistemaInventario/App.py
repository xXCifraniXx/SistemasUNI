from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, Response, flash, session
from flask_mysqldb import MySQL
from fpdf import FPDF

# initializations
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=30)

# Mysql Connection
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10415824'
app.config['MYSQL_PASSWORD'] = '3srUg3xvNn'
app.config['MYSQL_DB'] = 'sql10415824'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/', methods=["POST"])
def checkLogin():
    UN = request.form["Username"]
    PW = request.form["Password"]
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT usuario, password FROM usuarios WHERE usuario = %s AND password = %s', (UN, PW))
    data = list(cur.fetchall())
    if len(data) == 1:
        if data[0][1] == PW:
            session['Username'] = UN
            return render_template('sucursales.html')
        else:
            flash('Contraseña incorrecta.')
            return redirect('/')
    else:
        flash('No se puede encontrar el usuario o contraseña.')
        return redirect('/')


@app.route('/menu')
def Menu():
    if 'Username' in session:
        return render_template('sucursales.html')
    else: 
        return render_template('no_permission.html')

# Sucursal A
@app.route('/inventarioA')
def Index():
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursala')
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', sucursala=data)
    else: 
        return render_template('no_permission.html')


@app.route('/add_productA', methods=['POST'])
def add_product():
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            # if (cantidad.isdigit()) or (precio.isdigit()):
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO sucursala (nProducto, cantidad, precio) VALUES (%s,%s,%s)", (nProducto, cantidad, precio))
            mysql.connection.commit()
            #flash('Producto agregado con éxito', 'success')
            return redirect(url_for('Index'))
            # else:
            #   flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('Index'))
    else:
        return render_template('no_permission.html')

@app.route('/editA/<id>', methods=['POST', 'GET'])
def get_product(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM sucursala WHERE id = %s", (id,))
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit-product.html', product=data[0])
    else:
        return render_template('no_permission.html')

@app.route('/updateA/<id>', methods=['POST'])
def update_product(id):
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            if (cantidad.isalpha() == False and precio.isalpha() == False):
                cur = mysql.connection.cursor()
                cur.execute("""
                    UPDATE sucursala
                    SET nProducto = %s,
                        precio = %s,
                        cantidad = %s
                    WHERE id = %s
                """, (nProducto, precio, cantidad, id))
                flash('Producto actualizado con éxito', 'success')
                mysql.connection.commit()
            else:
                flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('Index'))
    else:
        return render_template('no_permission.html')


@app.route('/deleteA/<string:id>', methods=['POST', 'GET'])
def delete_product(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM sucursala WHERE id = {0}'.format(id))
        mysql.connection.commit()
        flash('Producto eliminado con éxito', 'warning')
        return redirect(url_for('Index'))
    else:
        return render_template('no_permission.html')

# Sucursal B
@app.route('/inventarioB')
def IndexB():
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursalb')
        data = cur.fetchall()
        cur.close()
        return render_template('SucursalB/indexB.html', sucursalb=data)
    else:
        return render_template('no_permission.html')

@app.route('/add_productB', methods=['POST'])
def add_productB():
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            # if (cantidad.isdigit()) and (precio.isdigit()):
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO sucursalb (nProducto, cantidad, precio) VALUES (%s,%s,%s)", (nProducto, cantidad, precio))
            mysql.connection.commit()
            flash('Producto agregado con éxito', 'success')
            return redirect(url_for('IndexB'))
            #else:
            #    flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('IndexB'))
    else:
        return render_template('no_permission.html')

@app.route('/editB/<id>', methods=['POST', 'GET'])
def get_productB(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM sucursalb WHERE id = %s", (id,))
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('SucursalB/edit-productB.html', product=data[0])
    else:
        return render_template('no_permission.html')

@app.route('/updateB/<id>', methods=['POST'])
def update_productB(id):
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            if (cantidad.isalpha() == False and precio.isalpha() == False):
                cur = mysql.connection.cursor()
                cur.execute("""
                    UPDATE sucursalb
                    SET nProducto = %s,
                        precio = %s,
                        cantidad = %s
                    WHERE id = %s
                """, (nProducto, precio, cantidad, id))
                flash('Producto actualizado con éxito', 'success')
                mysql.connection.commit()
            else:
                flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('IndexB'))
    else: 
        return render_template('no_permission.html')

@app.route('/deleteB/<string:id>', methods=['POST', 'GET'])
def delete_productB(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM sucursalb WHERE id = {0}'.format(id))
        mysql.connection.commit()
        flash('Producto eliminado con éxito', 'warning')
        return redirect(url_for('IndexB'))
    else: 
        return render_template('no_permission.html')
# Sucursal C


@app.route('/inventarioC')
def IndexC():
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursalc')
        data = cur.fetchall()
        cur.close()
        return render_template('SucursalC/indexC.html', sucursalc=data)
    else:
        return render_template('no_permission.html')


@app.route('/add_productC', methods=['POST'])
def add_productC():
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            #if (cantidad.isdigit()) and (precio.isdigit()):
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO sucursalc (nProducto, cantidad, precio) VALUES (%s,%s,%s)", (nProducto, cantidad, precio))
            mysql.connection.commit()
            flash('Producto agregado con éxito', 'success')
            return redirect(url_for('IndexC'))
            #else:
            #    flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('IndexC'))
    else: 
        return render_template('no_permission.html')

@app.route('/editC/<id>', methods=['POST', 'GET'])
def get_productC(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM sucursalc WHERE id = %s", (id,))
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('SucursalC/edit-productC.html', product=data[0])
    else:
        return render_template('no_permission.html')


@app.route('/updateC/<id>', methods=['POST'])
def update_productC(id):
    if 'Username' in session:
        if request.method == 'POST':
            nProducto = request.form['nProducto']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            if (cantidad.isalpha() == False and precio.isalpha() == False):
                cur = mysql.connection.cursor()
                cur.execute("""
                    UPDATE sucursalc
                    SET nProducto = %s,
                        precio = %s,
                        cantidad = %s
                    WHERE id = %s
                """, (nProducto, precio, cantidad, id))
                flash('Producto actualizado con éxito', 'success')
                mysql.connection.commit()
            else:
                flash('Inserte solo números para cantidad y precio', 'danger')
        return redirect(url_for('IndexC'))
    else: 
        return render_template('no_permission.html')


@app.route('/deleteC/<string:id>', methods=['POST', 'GET'])
def delete_productC(id):
    if 'Username' in session:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM sucursalc WHERE id = {0}'.format(id))
        mysql.connection.commit()
        flash('Producto eliminado con éxito', 'warning')
        return redirect(url_for('IndexC'))
    else:
        return render_template('no_permission.html')

@app.route('/downloadA/reportA/pdf')
def downloadA_reportA():
    if 'Username' in session:
        cur = None
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursala')
        data = cur.fetchall()
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'Productos', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width/4

        pdf.ln(1)

        th = pdf.font_size
        pdf.set_font('Courier', 'B', 12)
        pdf.cell(col_width, th, "ID", border=1)
        pdf.cell(col_width, th, "Nombre", border=1)
        pdf.cell(col_width, th, "Cantidad", border=1)
        pdf.cell(col_width, th, "Precio", border=1)
        pdf.ln(th)

        pdf.set_font('Courier', '', 12)
        for row in data:
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, str(row[1]), border=1)
            pdf.cell(col_width, th, str(row[2]), border=1)
            pdf.cell(col_width, th, str(row[3]), border=1)
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- fin de reporte -', align='C')
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'attachment;filename=productos.pdf'})
        cur.close()
    else:
        return render_template('no_permission.html')


@app.route('/downloadB/reportB/pdf')
def downloadB_reportB():
    if 'Username' in session:
        cur = None
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursalb')
        data = cur.fetchall()
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'Productos', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width/4

        pdf.ln(1)

        th = pdf.font_size
        pdf.set_font('Courier', 'B', 12)
        pdf.cell(col_width, th, "ID", border=1)
        pdf.cell(col_width, th, "Nombre", border=1)
        pdf.cell(col_width, th, "Cantidad", border=1)
        pdf.cell(col_width, th, "Precio", border=1)
        pdf.ln(th)

        pdf.set_font('Courier', '', 12)
        for row in data:
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, str(row[1]), border=1)
            pdf.cell(col_width, th, str(row[2]), border=1)
            pdf.cell(col_width, th, str(row[3]), border=1)
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- fin de reporte -', align='C')
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'attachment;filename=productos.pdf'})
        cur.close()
    else:
        return render_template('no_permission.html')


@app.route('/downloadC/reportC/pdf')
def downloadC_reportC():
    if 'Username' in session:
        cur = None
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sucursalc')
        data = cur.fetchall()
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'Productos', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width/4

        pdf.ln(1)

        th = pdf.font_size
        pdf.set_font('Courier', 'B', 12)
        pdf.cell(col_width, th, "ID", border=1)
        pdf.cell(col_width, th, "Nombre", border=1)
        pdf.cell(col_width, th, "Cantidad", border=1)
        pdf.cell(col_width, th, "Precio", border=1)
        pdf.ln(th)

        pdf.set_font('Courier', '', 12)
        for row in data:
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(col_width, th, str(row[1]), border=1)
            pdf.cell(col_width, th, str(row[2]), border=1)
            pdf.cell(col_width, th, str(row[3]), border=1)
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- fin de reporte -', align='C')
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'attachment;filename=productos.pdf'})
        cur.close()
    else:
        return render_template('no_permission.html')

def isFloat(n):
    return n == +n and n != (n|0)

def isInteger(n):
    return n == +n and n == (n|0)

@app.route('/logout')
def logout():
    session.pop('Username', None)
    return redirect("/")

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
