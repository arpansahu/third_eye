#!/bin/bash

# Third Eye - Local Development Setup Script
# This script sets up the database schema, runs migrations, and loads initial data

set -e  # Exit on error

echo "🔧 Third Eye - Local Development Setup"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}❌ Error: .env file not found!${NC}"
    echo "Please create .env file with proper credentials"
    exit 1
fi

echo -e "${GREEN}✓ .env file found${NC}"
echo ""

# Step 1: Check Python version
echo "📋 Step 1: Checking Python version..."
python --version
echo ""

# Step 2: Install dependencies
echo "📦 Step 2: Installing dependencies..."
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 3: Database Schema Setup
echo "💾 Step 3: Database Schema Setup"
echo "This project uses PostgreSQL with schema: third_eye"
echo "Database: arpansahu_one_db (shared across projects)"
echo ""
echo "Creating schema if it doesn't exist..."
echo ""
echo "Run this SQL command in your PostgreSQL database:"
echo "  psql -U postgres -h arpansahu.space -p 9552 -d arpansahu_one_db"
echo ""
echo "  # Create schema for third_eye"
echo "  CREATE SCHEMA IF NOT EXISTS third_eye;"
echo "  GRANT ALL ON SCHEMA third_eye TO postgres;"
echo "  \\q"
echo ""
read -p "Press Enter once you've created the schema (or if it already exists)..."
echo ""

# Step 4: Run migrations
echo "🔄 Step 4: Running database migrations..."
python manage.py makemigrations
python manage.py migrate
echo -e "${GREEN}✓ Migrations completed${NC}"
echo ""

# Step 5: Load initial data
echo "📊 Step 5: Loading initial data..."

# Load symptoms data
echo "Loading symptoms data..."
python manage.py update_symptoms_data
echo -e "${GREEN}✓ Symptoms data loaded${NC}"

# Load hospitals data (if CSV exists)
if [ -f "nin-health-facilities.csv" ]; then
    echo "Loading hospitals data from CSV..."
    python manage.py update_hospitals_data
    echo -e "${GREEN}✓ Hospitals data loaded${NC}"
else
    echo -e "${YELLOW}⚠ Hospital CSV file not found at root. Skipping hospitals data.${NC}"
fi

# Generate dummy patient data
echo "Generating dummy patient data..."
python manage.py generate_dummy_data --count=20
echo -e "${GREEN}✓ Dummy patient data generated${NC}"
echo ""

# Step 6: Collect static files
echo "🎨 Step 6: Collecting static files..."
python manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"
echo ""

# Summary
echo "======================================"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "======================================"
echo ""
echo "📝 Database Info:"
echo "  Host: arpansahu.space:9552"
echo "  Database: arpansahu_one_db"
echo "  Schema: third_eye"
echo ""
echo "📝 Next steps:"
echo "  1. Start the development server:"
echo "     ${GREEN}python manage.py runserver 8008${NC}"
echo ""
echo "  2. Access the application:"
echo "     ${GREEN}http://127.0.0.1:8008/${NC}"
echo ""
echo "  3. Access Django admin:"
echo "     ${GREEN}http://127.0.0.1:8008/admin/${NC}"
echo "     Username: admin"
echo "     Password: admin123"
echo ""
echo "Happy coding! 🚀"
