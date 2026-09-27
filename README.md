<a href="https://www.linkedin.com/in/ilyas-daoud-el-asmi-0a531039b">
  <img src="assets/header.svg" width="100%" alt="Ilyas Daoud El Asmi — AI Engineer (LLM fine-tuning, RAG, AI agents) building full-stack AI products, Oujda, Morocco" />
</a>

<p align="center">
  <a href="https://www.linkedin.com/in/ilyas-daoud-el-asmi-0a531039b"><img src="https://img.shields.io/badge/LinkedIn-Ilyas_Daoud_El_Asmi-E9A23B?style=for-the-badge&logo=linkedin&logoColor=E9A23B&labelColor=0E0C0A" alt="LinkedIn" /></a>
  <a href="mailto:idaoud361@gmail.com"><img src="https://img.shields.io/badge/Email-idaoud361@gmail.com-E9A23B?style=for-the-badge&logo=gmail&logoColor=E9A23B&labelColor=0E0C0A" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Based_in-Oujda,_Morocco-3DBF9F?style=for-the-badge&labelColor=0E0C0A" alt="Based in Oujda, Morocco" />
</p>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/s01-dark.svg" />
  <img src="assets/s01-light.svg" width="100%" alt="01 — About" />
</picture>

I'm an **AI Engineer** working on **LLM fine-tuning, RAG and AI agents**, and I build full-stack AI products end to end, from the data and the model to the interface a real person uses: **OMNIA**, **AtlasKick AI**, a **Darija LLM** and **Real or Clone?**. I hold a Bachelor in Data Analytics & BI from EST Oujda.

- **AI.** At LEADZ Tech Services I fine-tuned a conversational LLM for **Moroccan Darija**, then built a **RAG pipeline with OCR** for intelligent document processing.
- **Machine learning.** At CHU Mohammed VI I built a **deep-learning model to help detect breast anomalies on mammograms**, from image preprocessing to evaluation.
- **Full-stack.** React 19, Next.js and TypeScript on the front. Django REST Framework or NestJS with Prisma and PostgreSQL behind it. Docker, Playwright, deployed.
- **WEBZI1 Studio.** My studio designs and ships multilingual (FR / EN / AR) websites for cafés, restaurants and shops in Morocco and Brussels.

I work in Arabic (native), French and English, and I ship interfaces in all three, right-to-left included.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/s02-dark.svg" />
  <img src="assets/s02-light.svg" width="100%" alt="02 — Selected work" />
</picture>

<a href="https://github.com/ilyasdaoudrma/real-or-clone"><img src="assets/shots/real-or-clone.jpg" width="100%" alt="Real or Clone? — AI voice-clone scam detector" /></a>

### Real or Clone? &nbsp;·&nbsp; catching AI voice-clone scams in WhatsApp voice notes

Scammers need 3 seconds of audio to clone a voice and send a fake *"Mom, I had an accident, send money"* note. I **fine-tuned Meta's XLS-R 300M** on ~50,000 English and French clips turned into WhatsApp-style voice notes, including **1,619 fresh voice clones** I generated on an **NVIDIA L40S**. On held-out data it reaches **96.1% accuracy** and a **2.4% EER on cloning engines it never saw** (ElevenLabs, OpenAI, Gemini). My own tests caught a shortcut in the first model (it flagged 96% of real voices) and I fixed it, bringing false alarms down to ~7%. The app gives a verdict, the suspicious seconds and safety tips in Arabic, French or English, with Clerk login and a private history. Built in one day at the **GOMYCODE × NVIDIA** hackathon.

`PyTorch` `XLS-R 300M` `Chatterbox` `NVIDIA Brev` `FastAPI` `Clerk` `Groq`
&nbsp;→&nbsp; **[Code & results](https://github.com/ilyasdaoudrma/real-or-clone)** &nbsp;·&nbsp; **[90-s video](https://github.com/ilyasdaoudrma/real-or-clone/raw/main/web/demo.mp4)**

<br />

<a href="https://atlaskick-ai.vercel.app"><img src="assets/shots/atlaskick.jpg" width="100%" alt="AtlasKick AI — live site" /></a>

### AtlasKick AI &nbsp;·&nbsp; explainable World Cup 2026 match intelligence

Not "my AI predicts the winner." Every probability breaks down into named, quantified factors: an **Elo + Poisson + ML ensemble** with **SHAP explanations**, a **10,000-run Monte Carlo** tournament simulator, and a grounded AI analyst. It also has a dedicated Morocco mode. Runs entirely in the browser with no backend.

`React 19` `TypeScript` `Vite` `Tailwind v4` `Framer Motion` `Groq · Llama 3.3`
&nbsp;→&nbsp; **[Live](https://atlaskick-ai.vercel.app)** &nbsp;·&nbsp; **[Code](https://github.com/ilyasdaoudrma/atlaskick-ai)**

<br />

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://omnia-vert.vercel.app"><img src="assets/shots/omnia.jpg" width="100%" alt="OMNIA — live site" /></a>
      <h3>OMNIA</h3>
      <p>An agentic AI concierge you talk to in plain language. It plans and books across <b>stays, food and rides</b> in Morocco. It's <b>four full-stack apps sharing one Clerk login</b>: typed React frontends on NestJS + Prisma APIs over Neon Postgres, with rate limiting, server-to-server auth and a Playwright E2E suite.</p>
      <p><code>React 19</code> <code>NestJS</code> <code>Prisma</code> <code>PostgreSQL</code> <code>Groq</code></p>
      <p>→ <b><a href="https://omnia-vert.vercel.app">Live</a></b> · <b><a href="https://github.com/ilyasdaoudrma/omnia">Code</a></b></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://ascend-ai-chi.vercel.app"><img src="assets/shots/ascend.jpg" width="100%" alt="Ascend AI — live site" /></a>
      <h3>Ascend AI</h3>
      <p>A fitness tracker and social network for athletes, built end to end. I designed the relational schema, a <b>Django REST Framework</b> API with SimpleJWT, filtering, pagination and OpenAPI docs, and a <b>React 19</b> app on TanStack Query for workouts, analytics, feed and follows. The whole stack runs under Docker Compose.</p>
      <p><code>Django</code> <code>DRF</code> <code>PostgreSQL</code> <code>React 19</code> <code>Docker</code></p>
      <p>→ <b><a href="https://ascend-ai-chi.vercel.app">Live</a></b> · <b><a href="https://github.com/ilyasdaoudrma/ascend-ai">Code</a></b></p>
    </td>
  </tr>
</table>

#### Client work from WEBZI1 Studio

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://kami-coffee.vercel.app"><img src="assets/shots/kami.jpg" width="100%" alt="Kami Coffee — live site" /></a>
      <p><b>Kami</b>, a specialty coffee bar in Saint-Gilles, Brussels. Bilingual Next.js site with a full menu, reviews, a scroll-through "walk inside" and complete local SEO.</p>
      <p>→ <b><a href="https://kami-coffee.vercel.app">kami-coffee.vercel.app</a></b></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://mito-brugmann.vercel.app"><img src="assets/shots/mito.jpg" width="100%" alt="MiTo Brugmann — live site" /></a>
      <p><b>MiTo Brugmann</b>, an Italian trattoria in Ixelles, Brussels. Bilingual FR/EN rebuild with reservations, a priced menu, motion and structured data.</p>
      <p>→ <b><a href="https://mito-brugmann.vercel.app">mito-brugmann.vercel.app</a></b> · <a href="https://github.com/ilyasdaoudrma/mito-brugmann">Code</a></p>
    </td>
  </tr>
</table>

<details>
<summary><b>More from the lab</b>: private research, data work and smaller builds</summary>
<br />

| Project | What it is | Stack |
|---|---|---|
| **Gold Agent System** *(private)* | A simulation-only, multi-agent research platform for XAUUSD. Data, features, strategies, an LLM macro arbiter, sizing, risk, and backtest / walk-forward / stress testing. The honest result so far: technical-only strategies showed **no durable edge** on M15, H1 or H4, so it stays simulated while I add fundamental data. | Python · LLMs |
| **Instagram Engagement Analytics** | An ETL pipeline into a data warehouse, Random Forest classification and KMeans segmentation, feeding KPI dashboards. | Python · scikit-learn · Power BI |
| **Mammography anomaly detection** | Hospital internship project: deep-learning assistance for breast-anomaly detection, covering preprocessing and model evaluation. | Python · deep learning |
| **[Sunglasses S2L](https://sunglasses-s2l.vercel.app)** | An eyewear storefront concept with 3D product visuals. | Vite · Three.js |
| **[Dynamo Fit](https://dynamofit.vercel.app)** | A landing page for a gym in Salé, Morocco. | HTML · CSS · JS |

</details>

<br />

<img src="assets/divider.svg" width="100%" alt="" />

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/s03-dark.svg" />
  <img src="assets/s03-light.svg" width="100%" alt="03 — Experience" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg" />
  <img src="assets/timeline-light.svg" width="100%" alt="Experience: Founder of WEBZI1 Studio (2025–now); AI Intern at LEADZ Tech Services, Rabat (Apr–Jun 2026); Machine Learning Intern at CHU Mohammed VI, Oujda (Apr–May 2025); Web Development Intern at the Regional Health Directorate, Oujda (Jul 2024). Education: B.Sc. Data Analytics & Business Intelligence, EST Oujda (2025–2026); DUT Business Intelligence & Machine Learning, EST Oujda (2023–2025)." />
</picture>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/s04-dark.svg" />
  <img src="assets/s04-light.svg" width="100%" alt="04 — Toolbox" />
</picture>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,js,react,nextjs,vite,tailwind,threejs,nodejs,nestjs&perline=10" alt="Python, TypeScript, JavaScript, React, Next.js, Vite, Tailwind, Three.js, Node.js, NestJS" />
  <br />
  <img src="https://skillicons.dev/icons?i=django,prisma,postgres,mysql,sqlite,supabase,docker,tensorflow,sklearn,electron,git,vercel&perline=12" alt="Django, Prisma, PostgreSQL, MySQL, SQLite, Supabase, Docker, TensorFlow, scikit-learn, Electron, Git, Vercel" />
</p>

| | |
|---|---|
| **AI & data** | LLM fine-tuning · RAG · OCR · deep learning · scikit-learn · pandas · NumPy · ETL · data warehousing · Power BI |
| **Backend** | Django REST Framework · SimpleJWT · NestJS · Prisma · REST & OpenAPI · PostgreSQL / Neon · Supabase |
| **Frontend** | React 19 · Next.js App Router · TypeScript · TanStack Query · Zustand · Framer Motion · GSAP · Three.js |
| **Shipping** | Git & PR workflow · Docker Compose · Playwright E2E · Vercel · SEO & structured data · i18n with RTL |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/s05-dark.svg" />
  <img src="assets/s05-light.svg" width="100%" alt="05 — Let's talk" />
</picture>

I'm open to **AI, data and full-stack roles**, and to building a website for your business. The fastest way to reach me is **[LinkedIn](https://www.linkedin.com/in/ilyas-daoud-el-asmi-0a531039b)** or **[idaoud361@gmail.com](mailto:idaoud361@gmail.com)**.

<img src="assets/divider.svg" width="100%" alt="" />
