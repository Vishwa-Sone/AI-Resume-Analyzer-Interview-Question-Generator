import { useState, useRef } from 'react'

export default function UploadForm({ roles, loading, onSubmit }) {
  const [file, setFile] = useState(null)
  const [jobRole, setJobRole] = useState('')
  const [jobDesc, setJobDesc] = useState('')
  const [dragging, setDragging] = useState(false)
  const inputRef = useRef()

  const handleDrop = (e) => {
    e.preventDefault()
    setDragging(false)
    const dropped = e.dataTransfer.files[0]
    if (dropped) setFile(dropped)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!file || !jobRole) return
    onSubmit(file, jobRole, jobDesc)
  }

  return (
    <form className="card" onSubmit={handleSubmit} id="upload-form">
      <div className="card-title">
        <span className="icon">📄</span> Upload Resume
      </div>

      {/* File drop zone */}
      <div
        className={`file-drop ${dragging ? 'dragging' : ''}`}
        onDragOver={(e) => { e.preventDefault(); setDragging(true) }}
        onDragLeave={() => setDragging(false)}
        onDrop={handleDrop}
        onClick={() => inputRef.current.click()}
        id="file-drop-zone"
      >
        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.docx"
          hidden
          onChange={(e) => setFile(e.target.files[0])}
        />
        <p className="drop-text">
          Drop your resume here or <strong>browse</strong>
        </p>
        <p className="drop-text" style={{ fontSize: '0.76rem', marginTop: 4 }}>
          .pdf or .docx
        </p>
        {file && <p className="file-name">{file.name}</p>}
      </div>

      {/* Job Role */}
      <div className="form-group" style={{ marginTop: 18 }}>
        <label htmlFor="job-role">Target Job Role</label>
        <select
          id="job-role"
          value={jobRole}
          onChange={(e) => setJobRole(e.target.value)}
          required
        >
          <option value="">Select a role…</option>
          {roles.map((r) => (
            <option key={r} value={r}>
              {r.replace(/\b\w/g, (c) => c.toUpperCase())}
            </option>
          ))}
        </select>
      </div>

      {/* Job Description */}
      <div className="form-group">
        <label htmlFor="job-desc">Job Description (optional)</label>
        <textarea
          id="job-desc"
          placeholder="Paste the job description here…"
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
        />
      </div>

      {/* Submit */}
      <button
        type="submit"
        className="btn btn-primary"
        disabled={!file || !jobRole || loading}
        id="analyse-btn"
      >
        {loading ? (
          <>
            <span className="spinner" /> Analysing…
          </>
        ) : (
          'Analyse Resume'
        )}
      </button>
    </form>
  )
}
