import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from icecreamapp.models import Variety
from .connection import Connection


def home(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                v.id,
                v.name,
                v.country_of_origin
            FROM icecreamapp_variety v
            GROUP BY v.name
                        """)

            all_varieties = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                variety = Variety()
                variety.id = row['id']
                variety.name = row['name']
                variety.country_of_origin = row['country_of_origin']

                all_varieties.append(variety)

        template = 'home.html'
        context = {
            'varieties': all_varieties
        }

        return render(request, template, context)

