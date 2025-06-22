# Product Requirements Document (PRD)
## Mira: Digital Mirror for Personal Growth
### Hackathon Version 1.0

---

## 📋 Executive Summary

**Product Name**: Mira  
**Version**: Hackathon MVP 1.0  
**Team**: Team Mira  
**Duration**: 24-48 hour hackathon  
**Tagline**: "See yourself clearly, grow authentically"

### Vision Statement
Create a personalized growth companion that helps users understand how they're perceived online, bridge the gap between their current and ideal selves, and develop authentic personal growth strategies.

### Hackathon Goals
1. Demonstrate core concept with working prototype
2. Show clear differentiation from existing solutions
3. Create compelling demo for judges
4. Validate technical feasibility

---

## 🎯 Problem Statement

### Primary Problems
1. **Perception Gap**: People don't know how they come across online
2. **Generic Solutions**: Self-help apps provide one-size-fits-all advice
3. **Lack of Accountability**: No personalized follow-through on growth goals
4. **Feedback Vacuum**: Honest feedback from others is rare and difficult to obtain

### Target User Pain Points
- "I wonder if my LinkedIn profile makes me seem approachable or arrogant"
- "Self-help apps give me the same meditation everyone else gets"
- "I set goals but have no personalized accountability"
- "My friends won't tell me hard truths about myself"

---

## 👥 User Personas

### Primary Persona: "Growth-Oriented Professional"
- **Name**: Alex Chen
- **Age**: 28-35
- **Occupation**: Mid-level professional
- **Tech Savviness**: High
- **Goals**: Career advancement, authentic relationships, personal development
- **Frustrations**: Generic advice, lack of honest feedback, uncertainty about perception

### Secondary Persona: "Self-Aware Seeker"
- **Name**: Jordan Williams
- **Age**: 22-30
- **Occupation**: Creative/Freelancer
- **Tech Savviness**: Medium-High
- **Goals**: Understand authentic self, improve communication, build confidence
- **Frustrations**: Inconsistent online presence, manipulation concerns, finding mentors

---

## 📝 User Stories

### Must Have (P0 - For Hackathon)
1. As a user, I want to connect my LinkedIn profile so the system can analyze how I present professionally
2. As a user, I want to see a visual representation of my personality based on my online presence
3. As a user, I want to have a coaching conversation that references my specific traits
4. As a user, I want to see one actionable recommendation based on my analysis

### Should Have (P1 - Demo but not fully functional)
1. As a user, I want to see how my perception has changed over time
2. As a user, I want to request anonymous feedback from friends
3. As a user, I want to configure my "ideal self" based on chosen mentors

### Nice to Have (P2 - Vision features)
1. As a user, I want my personal AI model to learn from our conversations
2. As a user, I want to practice difficult conversations with my AI coach
3. As a user, I want to see my progress measured against psychological frameworks

---

## 🔧 Functional Requirements

### Core Features for Hackathon

#### 1. User Onboarding
- **Sign Up Flow**
  - Email/password registration
  - Terms acceptance
  - Quick personality quiz (3-5 questions)
- **Social Media Connection**
  - LinkedIn OAuth integration (primary)
  - Fallback: Manual URL input
  - Data consent screen

#### 2. Personality Analysis Engine
- **Data Collection**
  - Scrape public LinkedIn data (profile, posts, about)
  - Extract: job titles, skills, recommendations, post content
- **Analysis Output**
  - Personality traits (top 5)
  - Communication style
  - Professional "vibe" category
  - Confidence score

#### 3. Visualization Dashboard
- **Personality Radar Chart**
  - 5-8 dimensions (e.g., Leadership, Empathy, Innovation)
  - Current state visualization
  - Hover for details
- **Vibe Card**
  - Visual representation of overall impression
  - Key strengths and growth areas
  - Shareable format

#### 4. AI Coaching Interface
- **Chat Interface**
  - Clean, modern chat UI
  - System messages with personality insights
  - User input with suggestions
- **Personalized Responses**
  - Reference user's specific traits
  - Provide targeted advice
  - Suggest one concrete action

#### 5. Action Recommendation
- **Growth Suggestion**
  - One specific, actionable recommendation
  - Based on biggest gap or opportunity
  - Include resource (article, exercise, connection)

### Demo-Only Features (Simulated)

#### 6. Personal Model Training
- **Progress Visualization**
  - Show "learning from you" animation
  - Training progress bar
  - "Insights discovered" counter

#### 7. Anonymous Feedback Portal
- **Request Interface**
  - Generate shareable link
  - Show pending requests
  - Preview of feedback form

#### 8. Ideal Self Configuration
- **Mentor Selection**
  - Choose from preset options
  - Show influence percentage
  - Preview personality blend

---

## 💻 Technical Specifications

### Architecture Overview

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Frontend      │────▶│   Backend API   │────▶│   LLM Service   │
│   (React)       │     │   (Node.js)     │     │   (OpenAI)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌─────────────────┐
                        │   Database      │
                        │   (PostgreSQL)  │
                        └─────────────────┘
```

### Tech Stack
- **Frontend**: Astro + React + Tailwind CSS
- **Backend**: Supabase (BaaS) + Edge Functions
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Supabase Auth
- **LinkedIn Data**: RapidAPI LinkedIn API
- **AI/ML**: OpenAI API (GPT-4)
- **Hosting**: Vercel (perfect for Astro)

### API Endpoints

#### Supabase Setup
```sql
-- Users table (handled by Supabase Auth)

-- Profiles table
CREATE TABLE profiles (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  linkedin_url TEXT,
  linkedin_data JSONB,
  analysis_results JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Conversations table
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  messages JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;

-- RLS Policies
CREATE POLICY "Users can view own profile" ON profiles
  FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can view own conversations" ON conversations
  FOR ALL USING (auth.uid() = user_id);
```

#### Supabase Edge Functions
```javascript
// supabase/functions/analyze-linkedin/index.ts
export async function analyzeLinkedIn(linkedinUrl: string) {
  // Call RapidAPI
  const linkedinData = await fetchLinkedInData(linkedinUrl);
  // Process with OpenAI
  const analysis = await analyzePersonality(linkedinData);
  return analysis;
}

// supabase/functions/chat/index.ts
export async function handleChat(message: string, context: any) {
  // Process with OpenAI including user context
  const response = await generateCoachingResponse(message, context);
  return response;
}
```

#### RapidAPI LinkedIn Integration
```javascript
// LinkedIn data fetching
const options = {
  method: 'GET',
  url: 'https://linkedin-api.p.rapidapi.com/profile',
  params: { username: extractUsername(linkedinUrl) },
  headers: {
    'X-RapidAPI-Key': process.env.RAPIDAPI_KEY,
    'X-RapidAPI-Host': 'linkedin-api.p.rapidapi.com'
  }
};

const linkedinResponse = await axios.request(options);
```

### Frontend Architecture (Astro + React)

#### Astro Project Structure
```
src/
├── pages/
│   ├── index.astro          # Landing page
│   ├── dashboard.astro      # Analysis dashboard
│   ├── chat.astro          # Coaching interface
│   └── api/                # API routes (if needed)
├── components/
│   ├── react/
│   │   ├── PersonalityRadar.tsx
│   │   ├── ChatInterface.tsx
│   │   ├── VibeCard.tsx
│   │   └── ProgressTracker.tsx
│   └── astro/
│       ├── Layout.astro
│       ├── Header.astro
│       └── Footer.astro
├── lib/
│   ├── supabase.ts         # Supabase client
│   └── rapidapi.ts         # RapidAPI client
└── styles/
    └── global.css          # Tailwind CSS
```

#### Key Astro Benefits for Hackathon
- **Partial Hydration**: Only interactive components use React
- **Fast Build Times**: Better performance than pure React
- **SEO Friendly**: Great for landing page
- **Easy Deployment**: Works perfectly with Vercel

#### Supabase Client Setup
```typescript
// src/lib/supabase.ts
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  import.meta.env.PUBLIC_SUPABASE_URL,
  import.meta.env.PUBLIC_SUPABASE_ANON_KEY
)
```

---

## 🎨 UI/UX Requirements

### Design Principles
- **Modern & Clean**: Minimalist design with strong visual hierarchy
- **Trust-Building**: Professional but approachable
- **Data-Driven**: Visualizations that make insights clear
- **Mobile-Responsive**: Works on phone for demo

### Key Screens

#### 1. Landing Page
- Hero section with value prop
- "Connect LinkedIn" CTA
- Trust indicators (privacy, security)

#### 2. Analysis Dashboard
- Personality radar chart (full screen)
- Vibe card (shareable)
- Key insights (3 bullet points)
- "Start Coaching Session" button

#### 3. Coaching Chat
- Split screen: insights left, chat right
- Typing indicators
- Suggested responses
- Action items highlighted

#### 4. Progress View
- Timeline visualization
- "Model training" animation
- Future state preview

### Visual Design
- **Color Palette**: Deep purple (#6B46C1), teal accents (#14B8A6), neutral grays
- **Typography**: Inter for UI, Merriweather for quotes
- **Components**: Shadcn/ui components for consistency
- **Animations**: Subtle transitions, loading states

---

## 📊 Data Requirements

### Data Collection
- **LinkedIn Scraping**
  - Profile headline and summary
  - Recent posts (last 10)
  - Skills and endorsements
  - Recommendations text

### Data Processing
- **NLP Analysis**
  - Sentiment analysis on posts
  - Keyword extraction
  - Writing style analysis
  - Professional tone assessment

### Data Storage
- **User consent required**
- **Encryption at rest**
- **Right to deletion**
- **No PII in logs**

---

## 📈 Success Metrics

### Hackathon Judging Criteria
1. **Innovation**: Novel three-model approach
2. **Technical Implementation**: Working prototype
3. **User Experience**: Smooth demo flow
4. **Business Potential**: Clear monetization path
5. **Presentation**: Compelling story

### Demo Metrics
- Complete onboarding: < 2 minutes
- Time to first insight: < 30 seconds
- Coaching interaction: Natural and personalized
- Visual impact: "Wow" factor on analysis screen

---

## 🚧 Scope & Constraints

### In Scope for Hackathon
✅ LinkedIn integration (basic)  
✅ Personality analysis visualization  
✅ One coaching conversation  
✅ One action recommendation  
✅ Beautiful UI with 4-5 screens  

### Out of Scope for Hackathon
❌ Multiple social media platforms  
❌ Real model training  
❌ Anonymous feedback collection  
❌ Payment processing  
❌ Mobile app  

### Technical Constraints
- 24-48 hour development time
- Team of 4-5 people
- Limited API calls (use caching)
- No production infrastructure

---

## ⏱️ Timeline

### Hour-by-Hour Breakdown

**Hours 1-4: Setup & Planning**
- Team alignment on PRD
- Development environment setup
- UI/UX mockups created
- API keys obtained

**Hours 5-8: Core Backend**
- Authentication system
- LinkedIn scraping function
- Basic API endpoints
- Database setup

**Hours 9-12: Analysis Engine**
- NLP pipeline
- Personality calculation
- Data processing
- API integration

**Hours 13-16: Frontend Development**
- React app setup
- Dashboard UI
- Chat interface
- Responsive design

**Hours 17-20: Integration**
- Connect frontend/backend
- Debug data flow
- Polish interactions
- Add animations

**Hours 21-24: Demo Preparation**
- End-to-end testing
- Demo script
- Backup plans
- Pitch practice

---

## ⚠️ Risk Mitigation

### Technical Risks
- **LinkedIn API limits**: Pre-scraped demo data as backup
- **LLM API failures**: Cached responses for demo
- **Integration issues**: Modular architecture for independent progress

### Demo Risks
- **Live demo failure**: Recorded video backup
- **Network issues**: Local deployment option
- **Time constraints**: Core features first, enhance later

---

## 🎯 Definition of Done

### Hackathon MVP Checklist
- [ ] User can sign up and connect LinkedIn
- [ ] System generates personality analysis
- [ ] Dashboard displays visual insights
- [ ] User can have one coaching conversation
- [ ] System provides one action recommendation
- [ ] Demo flows smoothly end-to-end
- [ ] Pitch deck completed
- [ ] Code repository organized

### Judge-Ready Criteria
- [ ] 3-minute demo practiced
- [ ] Technical architecture explained
- [ ] Business model outlined
- [ ] Team roles clear
- [ ] Future vision compelling

---

## 📝 Appendix

### Quick Start Commands
```bash
# Create Astro project
npm create astro@latest mira-app -- --template minimal --typescript

# Install dependencies
cd mira-app
npm install @astrojs/react @astrojs/tailwind @supabase/supabase-js
npm install react react-dom @types/react @types/react-dom
npm install axios recharts lucide-react

# Setup Supabase
npx supabase init
npx supabase start  # For local development

# Environment variables (.env)
PUBLIC_SUPABASE_URL=your_supabase_url
PUBLIC_SUPABASE_ANON_KEY=your_anon_key
RAPIDAPI_KEY=your_rapidapi_key
OPENAI_API_KEY=your_openai_key

# Run development server
npm run dev
```

### Implementation Tips for Hackathon

#### 1. RapidAPI LinkedIn Integration
```typescript
// Quick implementation for profile fetching
export async function getLinkedInProfile(profileUrl: string) {
  const username = profileUrl.split('/in/')[1]?.replace('/', '');
  
  const options = {
    method: 'GET',
    url: 'https://linkedin-api.p.rapidapi.com/profile',
    params: { username },
    headers: {
      'X-RapidAPI-Key': import.meta.env.RAPIDAPI_KEY,
      'X-RapidAPI-Host': 'linkedin-api.p.rapidapi.com'
    }
  };
  
  try {
    const response = await axios.request(options);
    return response.data;
  } catch (error) {
    console.error('LinkedIn fetch error:', error);
    // Return mock data for demo
    return getMockLinkedInData();
  }
}
```

#### 2. Supabase Quick Wins
```typescript
// Authentication in 5 minutes
const { data, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password',
})

// Store profile data
const { data, error } = await supabase
  .from('profiles')
  .insert({
    user_id: user.id,
    linkedin_url: url,
    linkedin_data: linkedinData,
    analysis_results: analysis
  })
```

#### 3. React Component Example
```tsx
// src/components/react/PersonalityRadar.tsx
import { Radar } from 'recharts';

export function PersonalityRadar({ data }) {
  return (
    <div className="w-full h-96">
      <Radar data={data} />
    </div>
  );
}
```

### RapidAPI LinkedIn Data Processing

#### Key Fields to Extract
```typescript
interface LinkedInProfile {
  // Basic Info
  name: string;
  headline: string;
  summary: string;
  location: string;
  
  // Professional
  current_company: string;
  position: string;
  experience: Array<{
    title: string;
    company: string;
    description: string;
  }>;
  
  // Content
  about: string;
  skills: string[];
  recommendations: number;
  
  // Activity
  posts: Array<{
    text: string;
    likes: number;
    comments: number;
  }>;
}
```

#### Personality Analysis Mapping
```typescript
// Transform LinkedIn data to personality insights
function analyzePersonality(profile: LinkedInProfile) {
  const prompt = `
    Analyze this LinkedIn profile and provide:
    1. Top 5 personality traits
    2. Communication style (formal/casual/inspiring/analytical)
    3. Professional "vibe" (leader/collaborator/innovator/executor)
    4. One key strength and growth area
    
    Profile data: ${JSON.stringify(profile)}
  `;
  
  // Call OpenAI
  const analysis = await openai.createCompletion({
    model: "gpt-4",
    prompt,
    max_tokens: 500
  });
  
  return parseAnalysis(analysis);
}
```

#### Quick Personality Scoring
```typescript
// For hackathon speed, use keyword matching
const personalityKeywords = {
  leadership: ['led', 'managed', 'directed', 'founded'],
  innovation: ['created', 'developed', 'pioneered', 'launched'],
  collaboration: ['worked with', 'partnered', 'team', 'together'],
  analytical: ['analyzed', 'measured', 'optimized', 'data'],
  empathy: ['helped', 'supported', 'mentored', 'coached']
};
```