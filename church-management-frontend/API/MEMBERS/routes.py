from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session

members_bp = Blueprint("members_bp", __name__, template_folder='templates', static_folder='static')


@members_bp.route("/members", methods=["POST", "GET"])
def member_section():
    
    return render_template('member/members.html')

@members_bp.route("/add_member_form", methods=["POST", "GET"])
def admin_add():
    return render_template('member/add_member_form.html')

@members_bp.route("/view_member", methods=["POST", "GET"])
def admin_view():
    #members = Member.query.all()  # This retrieves all records from the Member table
    
    return render_template('member/view_member.html')
    # return render_template('member/view_member.html', members=members)