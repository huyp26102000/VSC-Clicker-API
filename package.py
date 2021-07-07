from flask import Flask, render_template, redirect, url_for, request, session, abort

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

import pathlib
import os
import json
import sys
import glob
import serial
import time, datetime
import uuid

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import credentials, db



cred = credentials.Certificate("./inspiration/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://clickervinschool-default-rtdb.firebaseio.com'})
tdb = firestore.client()
