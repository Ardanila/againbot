from aiogram import types
from typing import List

def make_row_keyboard(items: List[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in items]
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)