import { useState, useEffect } from 'react'
import UploadForm from './components/UploadForm'
import Results from './components/Results'

const API = 'http://localhost:8000'

export default function App() {
  const [roles, setRoles] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [result, setResult] = useState(null)

  useEffect(() => {
    fetch(`${API}/api/job-roles`)
      .then(r => r.json())
      .then(d => setRoles(d.roles))
      .catch(() => setRoles([]))
  }, [])

  const handleSubmit = async (file, jobRole, jobDescription) => {
    setLoading(true)
    setError(null)
    setResult(null)

    const formData = new FormData()
    formData.append('file', file)
    formData.append('job_role', jobRole)
    formData.append('job_description', jobDescription)

    try {
      const res = await fetch(`${API}/api/analyse`, {
        method: 'POST',
        body: formData,
      })

      if (!res.ok) {
        const err = await res.json().catch(() => ({}))
        if (res.status === 429) {
          throw new Error('API rate limit exceeded. Please wait a minute and try again.')
        }
        throw new Error(err.detail || 'Something went wrong')
      }

      const data = await res.json()
      setResult(data)
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setResult(null)
    setError(null)
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Resume Analyser</h1>
        <p>Upload your resume, pick a target role, and get AI-powered insights</p>
      </header>

      {error && <div className="error-box">{error}</div>}

      {!result ? (
        <UploadForm roles={roles} loading={loading} onSubmit={handleSubmit} />
      ) : (
        <Results data={result} onReset={handleReset} />
      )}
    </div>
  )
}
