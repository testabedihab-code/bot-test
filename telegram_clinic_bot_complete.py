#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Telegram Clinic Management System Bot
بوت تلغرام نظام إدارة العيادة
"""

import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import anthropic

# ============================================
# 🔧 الإعدادات
# ============================================

TELEGRAM_TOKEN = "8655171413:AAGMNPwcLjO5JDnVZXqAL1YoTgYmg3xy240"

# احصل على مفتاح API من متغير البيئة أو من متغير عام
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    print("❌ خطأ: لم يتم العثور على ANTHROPIC_API_KEY")
    print("يرجى تعيين متغير البيئة: ANTHROPIC_API_KEY")
    sys.exit(1)

# ============================================
# 📚 نص النظام (System Prompt)
# ============================================

SYSTEM_PROMPT = """You are a professional Sales Assistant for the "Clinic Management System" created by NOTE Software Company. Your role is to provide helpful, accurate, and professional information about the system's features and capabilities to potential clients and existing users.

## CLINIC MANAGEMENT SYSTEM OVERVIEW
