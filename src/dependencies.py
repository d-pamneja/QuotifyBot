import pandas as pd
import numpy as np
import sqlite3

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI
from dotenv import load_dotenv

import streamlit as st

os.environ.pop("OPENAI_API_KEY", None)
load_dotenv()
KEY = os.getenv("OPENAI_API_KEY")
print(KEY)