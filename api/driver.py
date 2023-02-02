from flask import request, jsonify
from configuration import db, function as fun
from configuration import request as rq
from configuration import response as res

def insert_the_driver():
    try:
        data = request.get_json()
        fname = data[rq.fname]
        lname = data[rq.lname]
        mobile = data[rq.mob_no]
        result = db.call_procedure(fun.insert_func, [fname, lname, mobile])
        response = []
        for row in result:
            response.append({res.code: row[0], res.message: row[1]})
            return jsonify(response)
    except Exception as e:
            return jsonify({'code': 500, 'msg': str(e)})


def select_the_driver():
    try:
        data = request.get_json()
        dID = data[rq.dri_id]
        fname = data[rq.fname]
        lname = data[rq.lname]
        mobno = data[rq.mob_no]
        result = db.call_procedure(fun.select_func, [dID, fname, lname, mobno])
        response = []
        for row in result:
            response.append({res.driv_id: row[0],
                             res.fname: row[1],
                             res.lname: row[2],
                             res.mob_no: row[3]})
        return jsonify(response)
    except Exception as e:
        return jsonify({'code': 500, 'msg fro  select exception': str(e)})


def delete_the_driver():
    try:
        data = request.get_json()
        driID = data[rq.dri_id]
        result = db.call_procedure(fun.delete_func, [driID])
        response = []
        for row in result:
            response.append({res.code: row[0], res.message: row[1]})
            return result
    except:
        return jsonify({'code': 500, 'msg': 'kuna error'})

def update_the_driver():
    try:
        data = request.get_json()
        dID = data[rq.dri_id]
        fname = data[rq.fname]
        lname = data[rq.lname]
        mobno = data[rq.mob_no]
        result = db.call_procedure(fun.update_func, [dID, fname, lname, mobno])
        response = []
        for row in result:
            response.append({res.code: row[0], res.message: row[1]})
            return jsonify(response)
    except:
        return jsonify({'code': 500, 'msg': 'kuna error'})