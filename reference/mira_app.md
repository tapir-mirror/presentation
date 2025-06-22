Mira - AI-Powered Personality Analysis & Vulnerability Assessment
React TypeScript Supabase Claude

🌟 Overview
Mira is an intelligent dual-analysis platform that helps professionals understand how they come across and protect themselves from manipulation based on their LinkedIn profiles. Using advanced AI analysis, Mira provides evidence-based personality insights, vulnerability assessments, and actionable protection strategies.

✨ Key Features
🧠 Dual Analysis System
🎯 Professional Analysis: Leadership indicators, collaboration style, and decision-making patterns
🛡️ Vulnerability Assessment: Seven Deadly Sins manipulation resistance analysis
🔍 Evidence-Based Insights: Every trait backed by specific quotes and examples from your profile
💡 Smart Technology
💰 Cost-Optimized: Intelligent caching reduces analysis costs by 70-80%
📊 Visual Analytics: Interactive personality radar charts and vulnerability dashboards
🔄 Smart Updates: Only re-analyzes when your profile meaningfully changes
🚫 Duplicate Prevention: Visual indicators prevent running the same analysis twice
🔒 Privacy & Security
🔐 Shared Knowledge: Analyzed profiles accessible to all authenticated users (prevents duplicate work)
🛡️ Self-Protection Focus: Vulnerability analysis designed for defensive awareness, not exploitation
🔒 Secure Data: Your authentication and usage data stays private
🚀 Quick Start
Prerequisites
Node.js 18+ and npm
Supabase account
Anthropic API key (for Claude)
RapidAPI key (for LinkedIn data)
Installation
Clone the repository
git clone https://github.com/tapir-mirror/mirror2.git
cd mirror2
Install dependencies
npm install
Set up environment variables
cp .env.example .env
Edit .env with your credentials:

VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
VITE_RAPIDAPI_KEY=your_rapidapi_key
VITE_ANTHROPIC_API_KEY=your_anthropic_api_key
Set up the database
Run the SQL migrations in your Supabase SQL editor:

-- Apply migrations in order:
-- 1. scope/mira_profiles_enhanced_simple.sql (base schema)
-- 2. supabase/migrations/003_separate_analyses.sql (new analysis table)
-- 3. supabase/migrations/004_fix_analyses_rls.sql (RLS policies)
-- 4. supabase/migrations/005_fix_analyses_insert_policy.sql (permissions)
Start the development servers
# In one terminal - start the API server
npm run dev:server

# In another terminal - start the React app
npm run dev

# Or run both together
npm run dev:full
Visit http://localhost:3000 to see the app!

🏗️ Architecture
Tech Stack
Frontend: React 18 + TypeScript + Tailwind CSS
Backend: Express.js (API proxy for Claude)
Database: Supabase (PostgreSQL)
AI: Claude 3.5 Sonnet (personality analysis)
Data Source: LinkedIn via RapidAPI
Project Structure
mirror2/
├── src/
│   ├── components/     # React components
│   ├── lib/           # Services and utilities
│   └── types/         # TypeScript interfaces
├── server.js          # Express API server
├── scope/             # Documentation and SQL
└── package.json       # Dependencies
📖 How It Works
1. Dual Analysis Flow

2. Intelligent Caching
Profile Hashing: Creates a unique hash of key profile elements
Change Detection: Only re-analyzes when profile significantly changes
Version Tracking: Re-analyzes when algorithm improves
Cost Monitoring: Tracks API usage and costs
3. Analysis Types
Professional Analysis
Each personality trait includes:

Specific Evidence: Quotes from your profile
Reasoning: Why this evidence supports the trait
Confidence Score: Based on evidence strength
Professional Context: Industry-specific interpretation
Vulnerability Assessment
Each vulnerability category includes:

Seven Deadly Sins Framework: Pride, Greed, Lust, Envy, Gluttony, Wrath, Sloth
Manipulation Patterns: How each vulnerability could be exploited
Protection Strategies: Specific awareness exercises and boundary recommendations
Risk Level: High/Medium/Low severity assessment
Red Flags: Warning signs to watch for in professional interactions
🔧 Configuration
API Endpoints
Core Endpoints:

POST /api/analyze - Professional personality analysis
POST /api/analyze-vulnerabilities - Vulnerability assessment using Seven Deadly Sins framework
Both endpoints check for existing analyses to prevent duplicates
Database Schema
The app uses three main tables:

mira_profiles

Stores LinkedIn profile data (shared across all users)
Tracks profile changes with content hashing
Fields: linkedin_url (unique), full_name, headline, summary, profile_picture_url
Status tracking: linkedin_data_status, linkedin_data_fetched_at
Legacy field: analysis_results (kept for backward compatibility)
mira_profile_analyses (New)

Stores different analysis types per profile
Fields: profile_id, analysis_type ('professional' | 'vulnerability'), analysis_results
Prevents duplicates: Unique constraint on (profile_id, analysis_type)
Tracks: analysis_version, analysis_cost, tokens_used
mira_conversations

Stores AI coaching conversations (legacy feature)
Enables personalized follow-up discussions
API Configuration
LinkedIn Data: Uses li-data-scraper via RapidAPI

Endpoint: https://li-data-scraper.p.rapidapi.com/get-profile-data-by-url
Extracts comprehensive profile data
AI Analysis: Claude 3.5 Sonnet via Anthropic API

Professional Analysis (/api/analyze): Evidence-based personality insights
Vulnerability Analysis (/api/analyze-vulnerabilities): Seven Deadly Sins manipulation assessment
Cost: ~$0.02-0.05 per analysis (each type)
Duplicate prevention: Check existing analyses before running
🛠️ Development
Running Tests
npm test
Building for Production
npm run build
Deployment
The app is optimized for Vercel deployment:

Connect your GitHub repo to Vercel
Add environment variables in Vercel dashboard
Deploy!
📊 Cost Optimization
The system includes several cost-saving features:

Smart Caching: Avoids re-analyzing unchanged profiles
Selective Refresh: Users choose when to update
Change Detection: Only analyzes meaningful changes
Token Tracking: Monitors API usage
Average costs:

Initial analysis: $0.02-0.05
Cached retrieval: $0 (no API calls)
Refresh (no changes): $0.001 (LinkedIn API only)
🔐 Privacy & Security
Shared Profile Model: Analyzed LinkedIn profiles are accessible to all authenticated users to prevent duplicate analysis work
Personal Data Protection: Your authentication details and usage history remain private
Row Level Security: Appropriate RLS policies for shared access model
Secure Authentication: Supabase Auth with email/password
Ethical AI: Vulnerability analysis designed for self-protection, not exploitation
API Key Protection: Server-side proxy for API calls
🤝 Contributing
Contributions are welcome! Please:

Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Open a pull request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Built with Claude by Anthropic
LinkedIn data via RapidAPI
Database by Supabase
UI components inspired by Tailwind UI
📞 Support
For issues or questions:

Open an issue on GitHub
Check the CLAUDE.md file for technical details
Review the SQL files in /scope for database setup
Built with ❤️ for the hackathon by Team Mira YEAH