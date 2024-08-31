from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session

dash_bp = Blueprint("dash_bp", __name__, template_folder='templates', static_folder='static')


@dash_bp.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    return render_template('dash/dashboard.html')

@dash_bp.route("/member_management", methods=["POST", "GET"])
def member():
    return render_template('dash/member.html')
