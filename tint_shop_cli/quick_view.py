#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('tint_shop.db')
cursor = conn.cursor()

print("CUSTOMERS:")
cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")

print("\nVEHICLES:")
cursor.execute("SELECT * FROM vehicles")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Customer: {row[1]}, {row[4]} {row[2]} {row[3]}, License: {row[5]}")

print("\nTINT JOBS:")
cursor.execute("SELECT * FROM tint_jobs")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Vehicle: {row[1]}, Service: {row[3]}, Cost: ${row[5]}")

print("\nPAYMENTS:")
cursor.execute("SELECT * FROM payments")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Job: {row[1]}, Amount: ${row[2]}, Method: {row[4]}")

conn.close()