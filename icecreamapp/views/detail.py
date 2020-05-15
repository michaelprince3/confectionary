import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from icecreamapp.models import Variety, Flavor
from .connection import Connection


def get_flavors(variety_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
            f.id,
            f.name
            FROM icecreamapp_flavor f
            
            """, (variety_id,))

        var_flavors = []
        data = db_cursor.fetchall()

        for row in data:
            flavor = Flavor()
            flavor.id = row['id']
            flavor.name = row['name']

            var_flavors.append(flavor)

        return var_flavors


def get_variety(variety_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            v.id,
            v.name,
            v.country_of_origin
        FROM icecreamapp_variety v
        WHERE v.id = ?
        """, (variety_id,))

        single_variety = []
        data = db_cursor.fetchone()

        for row in data:
            variety = Variety()
            variety.id = row['id']
            variety.name = row['name']
            variety.country_of_origin = row['country_of_origin']

            single_variety.append(variety)

        return single_variety


def detail(request, variety_id):
    if request.method == 'GET':
        variety = get_variety(variety_id)
        flavors = get_flavors(variety_id)

        template = 'detail.html'
        context = {
            'variety': variety,
            'flavors': flavors
        }

        return render(request, template, context)
