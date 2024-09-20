import pandas as pd
import numpy as np
import sqlite3

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))
import streamlit as st

load_dotenv()
KEY = os.getenv("OPENAI_API_KEY")
print(KEY)