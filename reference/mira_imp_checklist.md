# Mira Hackathon Implementation Checklist
## Quick Start Guide for Supabase + RapidAPI + Astro

### 🏃‍♂️ Hour 1: Initial Setup

#### Supabase Setup (15 min)
```bash
# Create new Supabase project at supabase.com
# Get your project URL and anon key
```

- [ ] Create Supabase account/project
- [ ] Copy project URL and anon key
- [ ] Enable Email Auth in Authentication settings

#### Astro + React Setup (15 min)
```bash
npm create astro@latest mira-app -- --template minimal --typescript
cd mira-app
npm install @astrojs/react @astrojs/tailwind @supabase/supabase-js
npm install react react-dom recharts lucide-react axios
npx astro add react tailwind
```

- [ ] Create Astro project
- [ ] Install all dependencies
- [ ] Verify dev server runs

#### Environment Setup (10 min)
Create `.env` file:
```
PUBLIC_SUPABASE_URL=your_url_here
PUBLIC_SUPABASE_ANON_KEY=your_key_here
RAPIDAPI_KEY=your_rapidapi_key
OPENAI_API_KEY=your_openai_key
```

- [ ] Get RapidAPI key from rapidapi.com
- [ ] Get OpenAI API key
- [ ] Add all to .env file

### 📊 Hour 2: Database Schema

Run in Supabase SQL Editor:
```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Profiles table
CREATE TABLE profiles (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  linkedin_url TEXT,
  linkedin_username TEXT,
  full_name TEXT,
  headline TEXT,
  linkedin_data JSONB,
  analysis_results JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Conversations table  
CREATE TABLE conversations (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  messages JSONB DEFAULT '[]'::jsonb,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Enable RLS
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;

-- Policies
CREATE POLICY "Users can CRUD own profile" ON profiles
  FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can CRUD own conversations" ON conversations
  FOR ALL USING (auth.uid() = user_id);
```

- [ ] Run schema in SQL editor
- [ ] Verify tables created
- [ ] Test RLS is enabled

### 🔧 Hour 3: Core Backend Functions

#### Create Supabase Client (`src/lib/supabase.ts`)
```typescript
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  import.meta.env.PUBLIC_SUPABASE_URL,
  import.meta.env.PUBLIC_SUPABASE_ANON_KEY
)
```

- [ ] Create supabase client
- [ ] Test connection

#### LinkedIn Fetcher (`src/lib/linkedin.ts`)
```typescript
import axios from 'axios';

export async function fetchLinkedInProfile(linkedinUrl: string) {
  // Extract username from URL
  const username = linkedinUrl.split('/in/')[1]?.replace('/', '');
  
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
    console.error('LinkedIn API error:', error);
    // Return mock data for demo
    return {
      name: "Demo User",
      headline: "Senior Software Engineer | AI Enthusiast",
      summary: "Passionate about building innovative solutions...",
      skills: ["React", "Node.js", "AI/ML", "Leadership"],
      experience: [{
        title: "Senior Developer",
        company: "Tech Corp",
        description: "Led team of 5 developers..."
      }]
    };
  }
}
```

- [ ] Create LinkedIn fetcher
- [ ] Test with real LinkedIn URL
- [ ] Implement mock data fallback

### 🎨 Hour 4-6: Frontend Pages

#### Landing Page (`src/pages/index.astro`)
```astro
---
import Layout from '../components/Layout.astro';
import { supabase } from '../lib/supabase';
---

<Layout title="Mira - See Yourself Clearly">
  <main class="min-h-screen bg-gradient-to-br from-purple-900 to-indigo-900">
    <div class="container mx-auto px-4 py-16">
      <h1 class="text-6xl font-bold text-white mb-6">
        See Yourself Clearly
      </h1>
      <p class="text-xl text-purple-200 mb-8">
        Understand how you're perceived online and grow authentically
      </p>
      <a href="/auth" class="bg-white text-purple-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-purple-100 transition">
        Connect Your LinkedIn
      </a>
    </div>
  </main>
</Layout>
```

- [ ] Create landing page
- [ ] Add hero section
- [ ] Link to auth page

#### Auth Page (`src/pages/auth.astro`)
```astro
---
import Layout from '../components/Layout.astro';
import AuthForm from '../components/react/AuthForm';
---

<Layout title="Sign In - Mira">
  <main class="min-h-screen flex items-center justify-center bg-gray-50">
    <AuthForm client:load />
  </main>
</Layout>
```

- [ ] Create auth page
- [ ] Implement AuthForm component
- [ ] Handle login/signup

### 🧠 Hour 7-9: Analysis Engine

#### Personality Analyzer (`src/lib/analyzer.ts`)
```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: import.meta.env.OPENAI_API_KEY,
});

export async function analyzeLinkedInProfile(profileData: any) {
  const prompt = `
    Analyze this LinkedIn profile and provide a JSON response with:
    {
      "personality_traits": ["trait1", "trait2", "trait3", "trait4", "trait5"],
      "communication_style": "formal|casual|inspiring|analytical",
      "vibe_category": "Leader|Innovator|Collaborator|Expert",
      "confidence_score": 0-100,
      "key_strength": "one sentence",
      "growth_area": "one sentence",
      "radar_data": [
        {"trait": "Leadership", "score": 0-100},
        {"trait": "Innovation", "score": 0-100},
        {"trait": "Empathy", "score": 0-100},
        {"trait": "Analytics", "score": 0-100},
        {"trait": "Communication", "score": 0-100}
      ]
    }
    
    Profile: ${JSON.stringify(profileData)}
  `;

  const completion = await openai.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: prompt }],
    response_format: { type: "json_object" }
  });

  return JSON.parse(completion.choices[0].message.content);
}
```

- [ ] Create analyzer function
- [ ] Test with sample data
- [ ] Handle errors gracefully

### 📊 Hour 10-12: Dashboard

#### Dashboard Page (`src/pages/dashboard.astro`)
```astro
---
import Layout from '../components/Layout.astro';
import PersonalityRadar from '../components/react/PersonalityRadar';
import VibeCard from '../components/react/VibeCard';
import { supabase } from '../lib/supabase';

// Get user profile data
const { data: { user } } = await supabase.auth.getUser();
const { data: profile } = await supabase
  .from('profiles')
  .select('*')
  .eq('user_id', user?.id)
  .single();
---

<Layout title="Your Analysis - Mira">
  <main class="min-h-screen bg-gray-50 p-8">
    <div class="max-w-6xl mx-auto">
      <h1 class="text-3xl font-bold mb-8">Your Personality Analysis</h1>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <PersonalityRadar data={profile?.analysis_results?.radar_data} client:load />
        <VibeCard analysis={profile?.analysis_results} client:load />
      </div>
      
      <div class="mt-8">
        <a href="/chat" class="bg-purple-600 text-white px-6 py-3 rounded-lg">
          Start Coaching Session
        </a>
      </div>
    </div>
  </main>
</Layout>
```

- [ ] Create dashboard layout
- [ ] Implement PersonalityRadar component
- [ ] Implement VibeCard component
- [ ] Add navigation to chat

### 💬 Hour 13-15: Chat Interface

#### Chat Component (`src/components/react/ChatInterface.tsx`)
```tsx
import { useState } from 'react';
import { supabase } from '../../lib/supabase';

export default function ChatInterface({ userProfile }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    // Add user message
    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);
    
    // Get AI response
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: input,
        context: userProfile.analysis_results
      })
    });
    
    const { reply } = await response.json();
    setMessages([...messages, userMessage, { role: 'assistant', content: reply }]);
    setInput('');
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, i) => (
          <div key={i} className={`mb-4 ${msg.role === 'user' ? 'text-right' : ''}`}>
            <div className={`inline-block p-3 rounded-lg ${
              msg.role === 'user' ? 'bg-purple-600 text-white' : 'bg-gray-200'
            }`}>
              {msg.content}
            </div>
          </div>
        ))}
      </div>
      
      <div className="border-t p-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 p-2 border rounded"
            placeholder="Ask your AI coach..."
          />
          <button onClick={sendMessage} className="px-4 py-2 bg-purple-600 text-white rounded">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
```

- [ ] Create chat interface
- [ ] Implement message handling
- [ ] Add typing indicators
- [ ] Store conversations

### 🚀 Hour 16-18: Deployment

#### Vercel Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

- [ ] Push to GitHub
- [ ] Connect Vercel to repo
- [ ] Add environment variables
- [ ] Deploy and test

### 🎭 Hour 19-20: Demo Preparation

#### Demo Checklist
- [ ] Create 3 test LinkedIn profiles
- [ ] Pre-generate analyses for smooth demo
- [ ] Prepare coaching conversation script
- [ ] Test on different devices
- [ ] Record backup video

#### Demo Flow (3 minutes)
1. **0:00-0:30** - Problem statement & solution
2. **0:30-1:00** - Live LinkedIn connection
3. **1:00-1:30** - Show personality analysis
4. **1:30-2:30** - Coaching conversation demo
5. **2:30-3:00** - Future vision & ask

### 🎯 Critical Success Factors

1. **Must Work**
   - [ ] Login/signup flow
   - [ ] LinkedIn data fetch
   - [ ] Personality visualization
   - [ ] One coaching interaction

2. **Nice to Have**
   - [ ] Multiple social platforms
   - [ ] Progress tracking
   - [ ] Anonymous feedback
   - [ ] Mobile responsive

3. **Demo Insurance**
   - [ ] Offline mode with cached data
   - [ ] Video backup of perfect flow
   - [ ] Static screenshots as fallback
   - [ ] Team member as "live user"

### 🔥 Final Hour Priorities

If running out of time, focus on:
1. **Visual Polish** - Make it look amazing
2. **Smooth Demo** - Practice the flow
3. **Clear Story** - Why this matters
4. **Working MVP** - Even if limited

Remember: Judges care more about vision and execution than perfect code!