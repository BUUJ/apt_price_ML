from flask import Blueprint, render_template, request, flash, jsonify
from .models import Predict
import json
from sqlalchemy import or_

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        seoul_gu = request.form.get('seoul_gu')
        seoul_dong = request.form.get('seoul_dong')
        apt_name = request.form.get('apt_name')
        apt_fl = request.form.get('apt_fl')

# 주소 검색
        target_apt = Predict.query.filter(
            or_(Predict.법정동주소.ilike(f'%{seoul_dong}%'))).first()
        apt_price = target_apt.단지명

# 아파트 위도 경도
        apt_location = {'latitude': target_apt.위도, 'longitude': target_apt.경도}

        return render_template("home.html", apt_price=apt_price, apt_location=json.dumps(apt_location, ensure_ascii=False))

    return render_template("home.html")
