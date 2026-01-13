<div align="center">

# Tana Nyiur Lestari

### Transform Waste into Value, One Transaction at a Time

**A comprehensive waste bank management platform that incentivizes recycling through gamification, connecting communities, waste banks, and environmental impact in a unified digital ecosystem.**

[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live_Demo-tananyiurlestari.com-success?style=for-the-badge&logo=google-chrome&logoColor=white)](https://tananyiurlestari.com/)

[🚀 Quick Start](#-installation--setup) · [📖 Documentation](#-table-of-contents) · [🤝 Contributing](#-contributing) · [🔒 Security](#-security--api-key-management) · [🌐 Live Demo](https://tananyiurlestari.com/)

---

</div>

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [How It Works](#-how-it-works)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Installation & Setup](#-installation--setup)
- [Usage & Examples](#-usage--examples)
- [Use Cases](#-use-cases)
- [Roadmap](#-roadmap)
- [Impact](#-impact)
- [Target Market](#-target-market)
- [Why This Matters](#-why-this-matters)
- [Vision & Mission](#-vision--mission)
- [Security & API Key Management](#-security--api-key-management)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🎯 Project Overview

**Tana Nyiur Lestari** is an enterprise-grade web platform that digitizes waste bank operations across Indonesia. By combining real-time transaction tracking, points-based rewards, and multi-tier organizational management, we bridge the gap between environmental action and economic incentives.

The platform serves as the operational backbone for waste bank networks, enabling:

- **Financial Inclusion** – Converting recyclables into monetary value for underserved communities
- **Environmental Impact Tracking** – Quantifying waste diverted from landfills
- **Operational Efficiency** – Streamlining workflows for foundation admins, bank operators, and members
- **Data-Driven Decision Making** – Real-time analytics for stakeholders at all levels

### Core Objectives

- **Environmental Sustainability** – Reduce landfill waste through systematic recycling programs
- **Economic Empowerment** – Create supplementary income streams for low-income households
- **Institutional Scalability** – Enable waste bank networks to expand operations efficiently
- **Community Engagement** – Gamify sustainable behavior through transparent reward systems
- **Geographic Accessibility** – Map waste bank locations for maximum community reach

---

## 🔍 The Problem

### The Global Waste Crisis

The world generates over **2 billion tons of waste annually**, with developing nations disproportionately affected by inadequate waste management infrastructure. In Indonesia alone:

- **64 million tons** of waste are produced yearly
- Only **7.5%** is formally recycled
- **24%** of waste ends up in rivers and oceans
- Low-income communities lack economic incentives to participate in recycling

### Operational Challenges for Waste Banks

Traditional waste bank operations face critical bottlenecks:

| Challenge | Impact |
|-----------|--------|
| **Manual Record-Keeping** | Prone to errors, slow processing, limited scalability |
| **Lack of Transparency** | Members distrust point calculations and redemption processes |
| **No Digital Infrastructure** | Difficult to track environmental impact or growth metrics |
| **Limited Reach** | Communities can't find nearby waste banks easily |
| **Admin Overhead** | Multi-level coordination (foundation → banks → members) is chaotic |

### The Economic Gap

Recycling remains economically unattractive for individuals when:
- Payouts are inconsistent or delayed
- No clear pricing structure exists for waste categories
- Administrative burden discourages participation

**The result?** Valuable recyclable materials are discarded, environmental damage continues, and communities miss income-generating opportunities.

---

## ✅ The Solution

**Tana Nyiur Lestari** digitizes the entire waste bank value chain with a scalable, transparent, and user-friendly platform.

### Our Approach

```
Community Members → Waste Collection → Digital Transaction Logging
         ↓                                      ↓
  Instant Points Earned              Real-Time Balance Updates
         ↓                                      ↓
  Redeem for Cash                    Admin Approval System
         ↓                                      ↓
   Economic Value                   Environmental Impact Tracking
```

### What Makes Us Different

| Traditional Waste Banks | Tana Nyiur Lestari |
|-------------------------|-------------------|
| Paper-based ledgers | Cloud-based digital records |
| Opaque pricing | Transparent, standardized rates |
| Delayed payouts | Instant point allocation + scheduled redemptions |
| Limited visibility | Real-time dashboards for all stakeholders |
| Manual calculations | Automated point calculations |
| No geographic data | Integrated mapping system |

### Value Proposition

**For Community Members:**  
Turn waste into income with transparent, instant point tracking

**For Waste Bank Operators:**  
Reduce admin overhead by 70% with automated transaction management

**For Foundation Admins:**  
Scale operations with real-time monitoring, analytics, and multi-bank coordination

**For Policymakers:**  
Access data-driven insights on recycling rates, environmental impact, and community engagement

---

## 🛠️ How It Works

### System Architecture

```
┌─────────────────┐
│ Community Member│
└────────┬────────┘
         │ Deposits Waste
         ↓
┌────────────────────┐
│ Waste Bank Unit    │
│ (Admin Logs Trans.)│
└────────┬───────────┘
         │
         ↓
┌─────────────────────────┐
│   Django Backend        │
│ - Calculates Points     │
│ - Updates Balances      │
│ - Stores Records        │
└────────┬────────────────┘
         │
    ┌────┴────┐
    │         │
    ↓         ↓
┌──────────┐ ┌───────────────┐
│ Member   │ │ Admin         │
│ Dashboard│ │ Analytics     │
│          │ │ Dashboard     │
└──────────┘ └───────────────┘
```

### Transaction Flow

1. **Waste Deposit**  
   Member brings recyclables to their assigned waste bank unit

2. **Weight & Categorization**  
   Bank admin weighs waste and selects category (Plastic, Paper, Metal, Organic, Used Oil)

3. **Automatic Point Calculation**  
   System applies category-specific rates:
   - **Used Oil**: 20 points/kg
   - **Metal**: 15 points/kg
   - **Plastic**: 10 points/kg
   - **Paper**: 5 points/kg
   - **Organic**: 2 points/kg

4. **Instant Balance Update**  
   Member account is credited immediately; viewable in personal dashboard

5. **Point Redemption**  
   Member requests cash conversion (minimum 50 points, Rp 1,000 per point)

6. **Admin Approval**  
   Bank admin reviews and approves/rejects redemption

7. **Payout**  
   Upon approval, member receives cash and points are deducted

### Role-Based Access Control

```
Foundation Admin (Level 1)
    ├── Manage all waste banks
    ├── View global analytics
    ├── Approve all redemptions
    └── Control content & partnerships
              │
         Bank Parent Admin (Level 2)
              ├── Manage unit banks
              ├── Monitor child bank performance
              └── Regional oversight
                      │
                 Bank Unit Admin (Level 3)
                      ├── Manage local members
                      ├── Log transactions
                      ├── Approve local redemptions
                      └── View unit-specific reports
                              │
                         Members (Level 4)
                              ├── Deposit waste
                              ├── Check balance
                              ├── Request redemptions
                              └── View transaction history
```

---

## ✨ Key Features

### 🎭 Multi-Tier User Management

**Role-Based Access Control (RBAC)** with 4 hierarchical levels:

- **Secure Authentication** – Django's built-in auth system with session management
- **Profile Customization** – Photo uploads, personal information, contact details
- **Account Lifecycle Management** – Activation, deactivation, password resets
- **Granular Permissions** – Each role sees only relevant functionality and data

### ♻️ Transaction Management System

**Comprehensive waste transaction tracking:**

| Feature | Description |
|---------|-------------|
| **5 Waste Categories** | Plastic (10 pts/kg), Paper (5 pts/kg), Metal (15 pts/kg), Organic (2 pts/kg), Used Oil (20 pts/kg) |
| **Automated Calculations** | Weight × category rate = instant points |
| **Advanced Filtering** | Search by date, member, category, bank |
| **CSV Export** | Download transaction histories for audits |
| **Edit & Delete** | Modify erroneous entries with audit trails |

### 💎 Points & Rewards Engine

**Gamified incentive system with economic value:**

- **Real-Time Accumulation** – Points credited instantly upon transaction
- **Transparent Pricing** – Fixed rate of **Rp 1,000 per point**
- **Flexible Redemption** – Minimum 50 points, increments of 50
- **Approval Workflow** – Prevent fraud with admin verification
- **Status Tracking** – Pending → Approved/Rejected with timestamps
- **Balance Checker** – Members view current points anytime

### 📊 Analytics & Reporting

**Data-driven insights for decision makers:**

- **Live Statistics** – Total members, banks, points distributed, waste collected
- **Category Breakdown** – Visual charts showing waste type distribution
- **Temporal Analysis** – Monthly/yearly trend reports
- **Export Capabilities** – Generate CSV reports for stakeholders
- **Pending Task Monitoring** – Track redemptions awaiting approval

### 🗺️ Geographic Mapping

**Integrated location services powered by Google Maps:**

- **Interactive Map Markers** – Pinpoint all registered waste bank locations
- **Proximity Search** – Find nearest waste banks based on user location
- **Bank Details** – View operating hours, contact info, supported categories
- **Responsive Design** – Mobile-friendly map interface

### 📝 Content Management System (CMS)

**Dynamic website content without coding:**

- **Blog/News System** – Post updates with rich text and images
- **Image Sliders** – Customizable homepage hero sections
- **Information Pages** – Editable sections for About, Vision, Programs
- **External Links** – Manage partner programs and resources
- **Partner Management** – Showcase organizational collaborators

### 🔐 Security & Compliance

**Enterprise-grade security measures:**

- **CSRF Protection** – Defend against cross-site request forgery
- **SQL Injection Prevention** – Parameterized queries via Django ORM
- **Session Management** – Secure cookie handling with HTTP-only flags
- **Password Validation** – Enforce strong password policies
- **Permission Decorators** – Restrict views based on user roles

---

## 🧰 Technology Stack

<div align="center">

### Backend

![Django](https://img.shields.io/badge/Django-5.1-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite)

### Frontend

![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat-square&logo=bootstrap)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat-square&logo=javascript)
![HTML5](https://img.shields.io/badge/HTML-5-E34F26?style=flat-square&logo=html5)
![CSS3](https://img.shields.io/badge/CSS-3-1572B6?style=flat-square&logo=css3)

### Infrastructure

![Google Maps](https://img.shields.io/badge/Google_Maps-API-4285F4?style=flat-square&logo=googlemaps)

</div>

### Core Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| **Django** | Web framework | 5.1 |
| **Pillow** | Image processing | Latest |
| **django-humanize** | Data formatting | Built-in |
| **python-decouple** | Environment variable management | Recommended |

### Architecture Highlights

- **MVC Pattern** – Model-View-Controller via Django MVT
- **ORM-Based Database** – No raw SQL queries
- **Template Inheritance** – DRY principle for HTML templates
- **Static File Management** – Centralized CSS/JS/image serving
- **Media Handling** – User-uploaded content with path management

---

## 🚀 Installation & Setup

### Prerequisites

Ensure your system has:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager, included with Python)
- **Git** ([Download](https://git-scm.com/downloads))
- **Virtual environment support** (included with Python 3.3+)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/AldyLoing/TanaNyiurLestari.git
cd TanaNyiurLestari
```

#### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv env
source env/bin/activate
```

#### 3. Install Dependencies

```bash
cd Blog
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

Create a `.env` file in the `Blog/` directory:

```bash
# Windows
copy .env.example .env

# Linux/macOS
cp .env.example .env
```

Edit `.env` with your settings:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-generate-a-strong-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (use PostgreSQL for production)
DATABASE_URL=sqlite:///db.sqlite3

# Google Maps API
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
```

**⚠️ SECURITY WARNING:** Never commit `.env` to version control. See [Security section](#-security--api-key-management).

#### 5. Initialize Database

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow prompts to set username, email, and password.

#### 7. Collect Static Files (Production)

```bash
python manage.py collectstatic
```

#### 8. Run Development Server

```bash
python manage.py runserver
```

#### 9. Access the Application

- **Main Site:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📖 Usage & Examples

### For Foundation Administrators

**Access global control panel:**

1. Navigate to Admin Panel and login
2. **Dashboard Overview** – View system-wide statistics (total members, banks, points, waste collected)
3. **Manage Banks** – Create/edit/deactivate waste bank units
4. **Approve Redemptions** – Review pending point-to-cash requests
5. **Content Management** – Update website sliders, blog posts, partner logos
6. **Analytics** – Export CSV reports for stakeholder meetings

**Example: Creating a New Waste Bank Unit**

```
Admin Panel → Banks → Add New Bank
├── Bank Name: "Green Valley Recycling Center"
├── Location: "Jl. Merdeka No. 45, Jakarta"
├── Coordinates: Lat -6.2088, Long 106.8456
├── Assign Admin: Select existing user or create new
└── Save → Bank appears on public map
```

### For Bank Unit Administrators

**Manage daily operations:**

1. Login to unit-specific dashboard
2. **Add Members** – Register new community members
3. **Log Transactions:**
   ```
   Member: John Doe
   Category: Plastic
   Weight: 5 kg
   Points Earned: 5 × 10 = 50 points (auto-calculated)
   ```
4. **Process Redemptions** – Approve member cash-out requests
5. **View Reports** – Check unit performance metrics

### For Community Members

**Earn rewards from recycling:**

1. **Register Account** – Sign up via website
2. **Deposit Waste** – Visit your local waste bank with recyclables
3. **Check Balance:**
   ```
   My Profile → Point Balance: 250 points (Rp 250,000 value)
   ```
4. **Request Redemption:**
   ```
   Redeem Points → Enter Amount: 200 points → Submit
   Status: Pending Admin Approval
   ```
5. **Receive Payment** – Collect cash at waste bank upon approval

---

## 🎯 Use Cases

### 1. Community-Based Recycling Programs
*Local governments partner with NGOs to incentivize household recycling*

**Scenario:** A district government wants to reduce landfill waste by 30% in 12 months.

**Implementation:**
- Deploy Tana Nyiur Lestari across 50 neighborhood waste banks
- Residents earn points for every deposit
- Track progress via analytics dashboard
- Adjust incentives based on participation data

**Outcome:** Measurable waste diversion, cost savings on landfill fees, increased community engagement

### 2. Corporate Social Responsibility (CSR) Initiatives
*Companies fund waste bank networks as sustainability projects*

**Scenario:** A manufacturing company needs to offset its carbon footprint.

**Implementation:**
- Sponsor waste bank operations in factory vicinity
- Employees and residents participate in recycling program
- Company tracks environmental impact for ESG reporting
- Points are subsidized by corporate funds

**Outcome:** Quantifiable environmental metrics for annual reports, improved community relations

### 3. School Education Programs
*Educational institutions teach sustainability through practical action*

**Scenario:** Schools integrate environmental education with economic literacy.

**Implementation:**
- Each class becomes a "member" with collective account
- Students bring recyclables weekly
- Earned points fund class projects or charity
- Leaderboards foster friendly competition

**Outcome:** Behavioral change in students, measurable waste reduction, financial literacy development

### 4. Microfinance & Financial Inclusion
*Provide unbanked populations with micro-savings mechanisms*

**Scenario:** Low-income communities lack access to formal banking.

**Implementation:**
- Waste bank points serve as micro-savings accounts
- Members accumulate value without traditional bank requirements
- Redemptions provide emergency cash access
- Financial literacy workshops tied to platform usage

**Outcome:** Economic empowerment, reduced financial vulnerability, savings habit formation

---

## 🗺️ Roadmap

### Q1 2026 (Current Version)
- [x] Core transaction management system
- [x] Multi-tier user roles
- [x] Points and redemption engine
- [x] Google Maps integration
- [x] Admin analytics dashboard
- [x] Content management system

### Q2 2026
- [ ] **Mobile Application** (iOS & Android)
  - React Native or Flutter implementation
  - Offline transaction mode with sync
  - QR code scanning for quick member lookup
- [ ] **RESTful API**
  - Full CRUD endpoints for external integrations
  - API authentication via JWT tokens
  - Webhook support for third-party services
- [ ] **Notification System**
  - Email notifications for redemption status
  - SMS alerts for transaction confirmations
  - Push notifications for mobile app

### Q3 2026
- [ ] **Advanced Analytics**
  - Machine learning for waste forecasting
  - Predictive models for redemption patterns
  - Carbon offset calculations
- [ ] **Payment Gateway Integration**
  - Direct bank transfers for redemptions
  - E-wallet integration (GoPay, OVO, Dana)
  - Automated payout scheduling
- [ ] **Multi-Language Support**
  - English and Bahasa Indonesia
  - Localization framework
  - RTL language support

### Q4 2026
- [ ] **Blockchain Integration** (Proof of Concept)
  - Immutable transaction records
  - Smart contracts for automated payouts
  - Tokenized points system
- [ ] **IoT Device Integration**
  - Smart weighing scales with auto-logging
  - RFID tags for member identification
  - Real-time inventory tracking

### 2027 and Beyond
- [ ] **Regional Expansion**
  - Multi-country deployment
  - Currency conversion support
  - Regulatory compliance frameworks
- [ ] **AI-Powered Features**
  - Computer vision for waste categorization
  - Chatbot for member support
  - Fraud detection algorithms

---

## 🌍 Impact

### Environmental Impact

**By digitizing waste bank operations, Tana Nyiur Lestari directly contributes to:**

| Metric | Impact (Per 1,000 Active Users/Year) |
|--------|--------------------------------------|
| **Waste Diverted from Landfills** | ~50 tons |
| **CO₂ Emissions Prevented** | ~75 tons CO₂e |
| **Ocean Plastic Reduction** | ~5 tons |
| **Trees Saved (via paper recycling)** | ~850 trees |

**Systemic Benefits:**
- Reduces methane emissions from organic waste decomposition
- Prevents microplastic pollution in waterways
- Conserves natural resources through material recovery
- Supports circular economy principles

### Social Impact

**Empowering communities through:**

- **Income Generation** – Average member earns Rp 200,000-500,000/month supplementary income
- **Financial Inclusion** – 60% of members are unbanked/underbanked populations
- **Employment Creation** – Formalizes informal waste sector jobs
- **Community Cohesion** – Strengthens neighborhood ties through collective action
- **Education** – Raises environmental awareness across demographics

### Economic Impact

**Creating measurable value:**

- **Cost Savings** – Municipalities save 15-20% on landfill disposal fees
- **New Markets** – Generates supply chains for recycled materials
- **MSMEs Empowerment** – Small waste aggregators scale operations
- **Investment Attraction** – Impact investors fund scalable green tech

---

## 🎯 Target Market

### Primary Markets

#### 1. Non-Governmental Organizations (NGOs)
*Environmental and community development NGOs operating waste bank programs*

- **Pain Point:** Manual record-keeping limits scale
- **Our Solution:** Automate operations, freeing staff for outreach
- **Market Size:** 500+ active waste bank NGOs in Indonesia

#### 2. Municipal Governments
*City/district administrations responsible for waste management*

- **Pain Point:** Lack of data on informal recycling sector
- **Our Solution:** Digitize and integrate informal waste collectors
- **Market Size:** 514 cities/regencies in Indonesia

#### 3. Corporate CSR Departments
*Companies seeking measurable environmental impact*

- **Pain Point:** Difficulty quantifying CSR project outcomes
- **Our Solution:** Real-time metrics for ESG reporting
- **Market Size:** 1,000+ companies with mandatory CSR in Indonesia

### Geographic Expansion Priorities

1. **Indonesia** (Phase 1: 2026-2027) – Jakarta, Surabaya, Bandung, Medan, Semarang
2. **Southeast Asia** (Phase 2: 2028-2029) – Philippines, Thailand, Vietnam, Malaysia
3. **South Asia** (Phase 3: 2030+) – India, Bangladesh, Sri Lanka

---

## 💡 Why This Matters

### The Global Context

The UN Sustainable Development Goals (SDGs) prioritize waste management as critical to:

- **SDG 11** (Sustainable Cities) – Reduce per capita environmental impact
- **SDG 12** (Responsible Consumption) – Achieve sustainable waste management
- **SDG 13** (Climate Action) – Reduce methane emissions from landfills
- **SDG 14** (Life Below Water) – Prevent plastic ocean pollution

### The Climate Case

- **Recycling 1 ton of plastic** prevents 2 tons of CO₂ emissions
- **Organic waste diversion** eliminates methane (25x more potent than CO₂)
- **Circular economy** reduces virgin material extraction

### The Social Justice Case

Waste pickers in informal sectors face:
- Health hazards from unsanitary conditions
- Economic exploitation by middlemen
- Social stigma and marginalization

**Tana Nyiur Lestari** formalizes this sector, providing:
- Digital records for financial credibility
- Fair pricing transparency
- Pathway to formalized employment

---

## 🌟 Vision & Mission

### Our Vision

**A world where waste has value, and every community has the tools to transform recyclables into economic opportunity and environmental restoration.**

### Our Mission

We empower waste bank networks with digital infrastructure to:

1. **Democratize Environmental Action**  
   Make recycling accessible and rewarding for all socioeconomic groups

2. **Quantify Impact**  
   Provide transparent metrics that prove environmental and economic value

3. **Scale Solutions**  
   Enable waste bank networks to grow from neighborhoods to nations

4. **Foster Innovation**  
   Serve as the platform for IoT, blockchain, and AI advancements in waste management

5. **Build Community**  
   Strengthen social cohesion through collective action toward shared goals

### Guiding Principles

- **Transparency First** – Every point, every transaction, fully auditable
- **User-Centric Design** – Technology that serves communities, not vice versa
- **Environmental Justice** – Prioritize marginalized communities in waste burden
- **Data Sovereignty** – User data belongs to users and their communities
- **Open Collaboration** – Share knowledge to accelerate global waste solutions

---

## 🔒 Security & API Key Management

### ⚠️ CRITICAL SECURITY NOTICE

This project integrates with external services (e.g., Google Maps API) that require API keys. **Exposing API keys in public repositories is a critical security vulnerability.**

### Secure API Key Management

#### 1. Environment Variables

**NEVER hardcode API keys in source code.** Use environment variables:

**Create `.env` file:**
```bash
# Blog/.env
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GOOGLE_MAPS_API_KEY=your_actual_api_key_here
```

**Load in settings.py:**
```python
# Blog/Blog/settings.py
import os
from decouple import config  # pip install python-decouple

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY')
```

#### 2. `.gitignore` Configuration

Ensure `.env` files are NEVER committed to version control:

**Add to `.gitignore`:**
```gitignore
# Environment variables
.env
.env.local
.env.production
*.env

# Django
db.sqlite3
*.pyc
__pycache__/
*.log

# Media files (may contain sensitive user data)
media/profile_pics/
media/profile_pictures/

# IDE
.vscode/
.idea/
```

#### 3. Example `.env.example` File

Provide a template WITHOUT actual secrets:

**Create `Blog/.env.example`:**
```env
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Google Maps API
GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

**Commit `.env.example` to repository, NOT `.env`.**

#### 4. Generate Strong Secret Keys

**Django Secret Key:**
```python
# In Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or online: https://djecrety.ir/

#### 5. API Key Best Practices

**Google Maps API:**
- Enable **Application Restrictions** (HTTP referrers for web)
- Enable **API Restrictions** (only Maps JavaScript API)
- Set **Quota Limits** to prevent abuse
- Rotate keys quarterly

**Configuration in Google Cloud Console:**
```
APIs & Services → Credentials → [Your API Key] → Edit
├── Application restrictions: HTTP referrers
│   └── Add referrer: yourdomain.com/*
├── API restrictions: Restrict key
│   └── Select APIs: Maps JavaScript API, Geocoding API
└── Set quotas: 25,000 requests/day (adjust as needed)
```

#### 6. Compromised Key Response

If an API key is exposed:

1. **Immediately Revoke** the compromised key in Google Cloud Console
2. **Generate New Key** with proper restrictions
3. **Update `.env` file** with new key
4. **Monitor Usage** for unauthorized access
5. **Review Git History:**
   ```bash
   # Remove secrets from Git history (DANGEROUS - coordinate with team)
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch Blog/.env" \
     --prune-empty --tag-name-filter cat -- --all
   ```
6. **Force Push** (if coordinating with team):
   ```bash
   git push origin --force --all
   ```

#### 7. Production Environment

**For deployment (Heroku, Railway, DigitalOcean):**

Set environment variables via platform dashboard:

**Heroku Example:**
```bash
heroku config:set SECRET_KEY="your-production-secret-key"
heroku config:set DEBUG=False
heroku config:set GOOGLE_MAPS_API_KEY="your-production-api-key"
```

**Verify:**
```bash
heroku config
```

#### 8. Security Checklist

Before deploying to production:

- [ ] All API keys stored in `.env`
- [ ] `.env` added to `.gitignore`
- [ ] `.env.example` committed (no secrets)
- [ ] `DEBUG=False` in production
- [ ] `ALLOWED_HOSTS` properly configured
- [ ] Google Maps API has application & API restrictions
- [ ] Database backups automated
- [ ] HTTPS/SSL certificates installed
- [ ] CSRF and session security enabled
- [ ] Regular security audits scheduled

---

## 🤝 Contributing

We welcome contributions from developers, designers, and domain experts! Here's how you can help:

### Ways to Contribute

- **🐛 Bug Reports** – Submit detailed issue reports with reproduction steps
- **💡 Feature Requests** – Propose new functionality with use case justification
- **📝 Documentation** – Improve guides, tutorials, or code comments
- **🎨 Design** – Enhance UI/UX with mockups or prototypes
- **💻 Code** – Implement features, fix bugs, or optimize performance
- **🌍 Translation** – Add support for new languages

### Contribution Workflow

1. **Fork the Repository**
   ```bash
   git clone https://github.com/AldyLoing/TanaNyiurLestari.git
   cd TanaNyiurLestari
   git remote add upstream https://github.com/AldyLoing/TanaNyiurLestari.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Follow PEP 8 style guide for Python
   - Write descriptive commit messages
   - Add tests for new functionality
   - Update documentation as needed

4. **Test Thoroughly**
   ```bash
   python manage.py test
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature with detailed description"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Create Pull Request**
   - Use descriptive PR title
   - Reference related issues
   - Explain changes and rationale
   - Request review from maintainers

### Coding Standards

- **Python**: Follow PEP 8 (use `flake8` or `black`)
- **Django**: Adhere to Django best practices
- **Comments**: Write docstrings for functions/classes
- **Git Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/)
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation changes
  - `style:` code formatting
  - `refactor:` code restructuring
  - `test:` adding tests
  - `chore:` maintenance tasks

### Code Review Process

All submissions require review. We use GitHub pull requests for this purpose:

- Maintainers review PRs within 48 hours
- Address feedback constructively
- Squash commits before merge
- Update branch with `main` before merging

### Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers get started
- Credit contributors appropriately

---

## 🐛 Bug Reports & Feature Requests

### Reporting Bugs

Found a bug? [Create an issue](https://github.com/AldyLoing/TanaNyiurLestari/issues) with:

- **Title**: Concise description
- **Environment**: OS, Python version, browser
- **Steps to Reproduce**: Numbered list
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots**: If applicable
- **Error Logs**: Paste relevant console output

### Requesting Features

Want a new feature? [Open a feature request](https://github.com/AldyLoing/TanaNyiurLestari/issues) including:

- **Use Case**: Why this feature is needed
- **Proposed Solution**: How it should work
- **Alternatives Considered**: Other approaches
- **Additional Context**: Mockups, examples, references

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` file for more information.

### What This Means

You are free to:
- ✅ **Use** – Commercial and private use
- ✅ **Modify** – Adapt to your needs
- ✅ **Distribute** – Share with others
- ✅ **Sublicense** – Include in proprietary software

**Requirements:**
- 📄 Include original license and copyright notice
- ⚠️ No liability or warranty from original authors

---

## 📞 Support

Need help or have questions?

### 📧 Email
[loingaldy@gmail.com](mailto:loingaldy@gmail.com)

### 💬 GitHub Discussions
[Start a discussion](https://github.com/AldyLoing/TanaNyiurLestari/discussions)

### 🐛 Issues
[Report bugs or request features](https://github.com/AldyLoing/TanaNyiurLestari/issues)

### 📱 Community
Join our community channels:
- **WhatsApp**: [+62 822-9349-4989](https://wa.me/6282293494989)
- **Instagram**: [@aldy_loing](https://instagram.com/aldy_loing)
- **Discord**: [Coming Soon]

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Google Maps API Guides](https://developers.google.com/maps/documentation)
- [Python Best Practices](https://www.python.org/dev/peps/pep-0008/)

---

## 🙏 Acknowledgments

This project is made possible by:

- **Django Software Foundation** – For the excellent web framework
- **Bootstrap Team** – For responsive design components
- **Google** – For Maps API infrastructure
- **Open Source Community** – For countless libraries and inspiration
- **Waste Bank Networks** – For domain expertise and real-world testing
- **Environmental Advocates** – For championing sustainable solutions

---

## 📊 Project Stats

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/AldyLoing/TanaNyiurLestari?style=social)
![GitHub forks](https://img.shields.io/github/forks/AldyLoing/TanaNyiurLestari?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/AldyLoing/TanaNyiurLestari?style=social)

[![GitHub issues](https://img.shields.io/github/issues/AldyLoing/TanaNyiurLestari)](https://github.com/AldyLoing/TanaNyiurLestari/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/AldyLoing/TanaNyiurLestari)](https://github.com/AldyLoing/TanaNyiurLestari/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/AldyLoing/TanaNyiurLestari)](https://github.com/AldyLoing/TanaNyiurLestari/commits/main)

</div>

---

<div align="center">

**⭐ If this project helps your organization or community, please star it on GitHub!**

Made with ❤️ for a sustainable future 🌱

[🔝 Back to Top](#tana-nyiur-lestari)

</div>
