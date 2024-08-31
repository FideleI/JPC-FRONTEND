from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session

index_bp = Blueprint("index_bp", __name__, template_folder='templates', static_folder='static')


@index_bp.route("/", methods=["POST", "GET"])
def index():
    return render_template('home/index.html')

@index_bp.route("/member_form", methods=["POST", "GET"])
def member_register():
    return render_template('home/member_form.html')

@index_bp.route("/visitors_form", methods=["POST", "GET"])
def visitors_register():
    return render_template('home/visitors_form.html')

@index_bp.route("/workforce_form", methods=["POST", "GET"])
def workforce_register():
    return render_template('home/workforce_form.html')