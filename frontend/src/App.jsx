import { useMemo, useState } from 'react'

const wizardSteps = [
  'Upload & ingest documents',
  'Summarize case file',
  'Identify legal issues',
  'Map guided analysis plan',
  'Collect party and relationship info',
  'Outline procedural history',
  'Capture evidence and exhibits',
  'Surface statutes and rules',
  'Draft arguments and counterarguments',
  'Evaluate outcomes and remedies',
  'Generate court forms',
  'Detect rules & deadlines',
  'Schedule reminders',
  'Match legal aid resources',
  'Compare declarations and disputes',
]

export default function App() {
  const [currentStepIndex, setCurrentStepIndex] = useState(0)

  const currentStep = useMemo(() => wizardSteps[currentStepIndex], [currentStepIndex])

  return (
    <div className="app">
      <header className="app__header">
        <h1>Family Law Case Analysis Wizard</h1>
        <p>A guided experience for steps 1–15 of the case analysis workflow.</p>
      </header>
      <main className="layout">
        <nav className="sidebar" aria-label="Wizard steps">
          <ol>
            {wizardSteps.map((step, index) => (
              <li key={step} className={index === currentStepIndex ? 'active' : ''}>
                <button type="button" onClick={() => setCurrentStepIndex(index)}>
                  <span className="step-number">{index + 1}</span>
                  <span className="step-title">{step}</span>
                </button>
              </li>
            ))}
          </ol>
        </nav>
        <section className="content" aria-live="polite">
          <h2>
            Step {currentStepIndex + 1}: {currentStep}
          </h2>
          <p>
            This is a placeholder for the guided workflow. Each step will collect inputs, surface recommendations,
            and connect to backend services for summarization, classification, and reminders.
          </p>
          <div className="actions">
            <button
              type="button"
              onClick={() => setCurrentStepIndex((index) => Math.max(index - 1, 0))}
              disabled={currentStepIndex === 0}
            >
              Previous
            </button>
            <button
              type="button"
              onClick={() => setCurrentStepIndex((index) => Math.min(index + 1, wizardSteps.length - 1))}
              disabled={currentStepIndex === wizardSteps.length - 1}
            >
              Next
            </button>
          </div>
        </section>
      </main>
    </div>
  )
}
