from flask import Flask, render_template, redirect, url_for, request, session, abort

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import credentials, db



cred = credentials.Certificate("./inspiration/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://clickervinschool-default-rtdb.firebaseio.com'})
tdb = firestore.client()
