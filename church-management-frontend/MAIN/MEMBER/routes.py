from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session

member_bp = Blueprint("member_bp", __name__, template_folder='templates', static_folder='static')


@member_bp.route("/members", methods=["POST", "GET"])
def member_section():
    
    return render_template('member/members.html')