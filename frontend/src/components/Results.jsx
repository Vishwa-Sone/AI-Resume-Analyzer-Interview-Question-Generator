import { useState } from 'react'
import { jsPDF } from 'jspdf'
import MatchRing from './MatchRing'

/* ── Helper: format an education item ─────────────────── */
function formatEducation(item) {
  if (typeof item === 'string') return item
  const parts = []
  if (item.degree) parts.push(item.degree)
  if (item.institution) parts.push(item.institution)
  if (item.year) parts.push(item.year)
  return parts.length > 0 ? parts.join(' — ') : JSON.stringify(item)
}

/* ── Helper: format an experience item ────────────────── */
function formatExperienceTitle(item) {
  if (typeof item === 'string') return { title: item, desc: '' }
  const title = [item.title, item.company, item.duration].filter(Boolean).join(' · ')
  return { title: title || 'Untitled', desc: item.description || '' }
}

export default function Results({ data, onReset }) {
  const [section, setSection] = useState('resume')
  const [tab, setTab] = useState('overview')
  const { parsed, match, qa } = data

  /* ── PDF helper: add text with auto-page-break ──────── */
  const addText = (doc, text, x, y, maxWidth) => {
    const pageHeight = doc.internal.pageSize.getHeight()
    const margin = 20
    if (y > pageHeight - margin) {
      doc.addPage()
      y = margin
    }
    if (maxWidth) {
      const lines = doc.splitTextToSize(text, maxWidth)
      lines.forEach((line) => {
        if (y > pageHeight - margin) {
          doc.addPage()
          y = margin
        }
        doc.text(line, x, y)
        y += 6
      })
    } else {
      doc.text(text, x, y)
      y += 6
    }
    return y
  }

  const downloadReport = () => {
    const doc = new jsPDF()
    const pageWidth = doc.internal.pageSize.getWidth()
    const maxW = pageWidth - 40
    let y = 20

    // Title
    doc.setFontSize(20)
    y = addText(doc, 'Resume Analysis Report', 20, y)
    y += 6

    // Date
    doc.setFontSize(11)
    y = addText(doc, `Generated on: ${new Date().toLocaleDateString()}`, 20, y)
    y += 8

    // ─── Personal Info ───
    doc.setFontSize(15)
    y = addText(doc, 'Personal Information', 20, y)
    y += 2
    doc.setFontSize(11)
    if (parsed.name) y = addText(doc, `Name: ${parsed.name}`, 20, y)
    if (parsed.email) y = addText(doc, `Email: ${parsed.email}`, 20, y)
    if (parsed.phone) y = addText(doc, `Phone: ${parsed.phone}`, 20, y)
    if (parsed.linkedin) y = addText(doc, `LinkedIn: ${parsed.linkedin}`, 20, y)
    if (parsed.github) y = addText(doc, `GitHub: ${parsed.github}`, 20, y)
    if (parsed.skills?.length > 0) y = addText(doc, `Skills Found: ${parsed.skills.length}`, 20, y)
    if (parsed.all_skills?.length > 0) {
      y = addText(doc, `All Skills: ${parsed.all_skills.join(', ')}`, 20, y, maxW)
    }
    y += 6

    // ─── Skill Match ───
    doc.setFontSize(15)
    y = addText(doc, 'Skill Match', 20, y)
    y += 2
    doc.setFontSize(11)
    y = addText(doc, `${match.percentage}% Match`, 20, y)
    y = addText(doc, `${match.found.length} of ${match.found.length + match.missing.length} required skills found`, 20, y)

    if (match.found.length > 0) {
      y += 2
      y = addText(doc, 'Found Skills:', 20, y)
      match.found.forEach((skill) => {
        y = addText(doc, `• ${skill}`, 25, y)
      })
    }
    if (match.missing.length > 0) {
      y += 2
      y = addText(doc, 'Missing Skills:', 20, y)
      match.missing.forEach((skill) => {
        y = addText(doc, `• ${skill}`, 25, y)
      })
    }
    y += 6

    // ─── Education ───
    if (parsed.education?.length > 0) {
      doc.setFontSize(15)
      y = addText(doc, 'Education', 20, y)
      y += 2
      doc.setFontSize(11)
      parsed.education.forEach((item) => {
        y = addText(doc, `• ${formatEducation(item)}`, 25, y, maxW)
      })
      y += 6
    }

    // ─── Experience ───
    if (parsed.experience?.length > 0) {
      doc.setFontSize(15)
      y = addText(doc, 'Experience', 20, y)
      y += 2
      doc.setFontSize(11)
      parsed.experience.forEach((item) => {
        const { title, desc } = formatExperienceTitle(item)
        y = addText(doc, `• ${title}`, 25, y, maxW)
        if (desc) y = addText(doc, `  ${desc}`, 28, y, maxW)
      })
      y += 6
    }

    // ─── Projects ───
    if (parsed.projects?.length > 0) {
      doc.setFontSize(15)
      y = addText(doc, 'Projects', 20, y)
      y += 2
      doc.setFontSize(11)
      parsed.projects.forEach((p) => {
        const title = p.title || 'Untitled'
        y = addText(doc, `• ${title}`, 25, y, maxW)
        if (p.description) y = addText(doc, `  ${p.description}`, 28, y, maxW)
        if (p.technologies?.length > 0) {
          y = addText(doc, `  Tech: ${p.technologies.join(', ')}`, 28, y, maxW)
        }
      })
      y += 6
    }

    // ─── Certifications ───
    if (parsed.certifications?.length > 0) {
      doc.setFontSize(15)
      y = addText(doc, 'Certifications', 20, y)
      y += 2
      doc.setFontSize(11)
      parsed.certifications.forEach((c) => {
        const text = typeof c === 'string' ? c : (c.name || JSON.stringify(c))
        y = addText(doc, `• ${text}`, 25, y, maxW)
      })
      y += 6
    }

    // ─── AI Insights ───
    if (qa && !qa.error) {
      doc.setFontSize(15)
      y = addText(doc, 'AI Insights', 20, y)
      y += 2
      doc.setFontSize(11)

      if (qa.missing_skills?.length > 0) {
        y = addText(doc, 'Missing Skills:', 20, y)
        qa.missing_skills.forEach((item) => {
          y = addText(doc, `• ${item.skill} (${item.priority || 'low'}): ${item.reason}`, 25, y, maxW)
        })
        y += 4
      }

      if (qa.project_suggestions?.length > 0) {
        y = addText(doc, 'Project Suggestions:', 20, y)
        qa.project_suggestions.forEach((p) => {
          y = addText(doc, `• ${p.title} (${p.difficulty}): ${p.description}`, 25, y, maxW)
          if (p.skills_targeted?.length > 0) {
            y = addText(doc, `  Skills: ${p.skills_targeted.join(', ')}`, 28, y, maxW)
          }
        })
        y += 4
      }

      if (qa.interview_QA?.length > 0) {
        y = addText(doc, 'Interview Q&A:', 20, y)
        qa.interview_QA.forEach((q) => {
          y = addText(doc, `Q: ${q.question}`, 25, y, maxW)
          y = addText(doc, `A: ${q.answer}`, 25, y, maxW)
          y += 2
        })
      }
    }

    doc.save('resume-analysis-report.pdf')
  }

  // Count improvements
  const missingCount = qa?.missing_skills?.length || 0
  const projectCount = qa?.project_suggestions?.length || 0
  const interviewCount = qa?.interview_QA?.length || 0
  const totalImprovements = missingCount + projectCount + interviewCount

  return (
    <>
      {/* ── Section Toggle ──────────────────────────── */}
      <div className="section-toggle-wrapper">
        <div className="section-toggle" id="section-toggle">
          <button
            className={`section-toggle-btn ${section === 'resume' ? 'active' : ''}`}
            onClick={() => setSection('resume')}
            type="button"
            id="toggle-resume-details"
          >
            <span className="section-toggle-icon">📄</span>
            Resume Details
          </button>
          <button
            className={`section-toggle-btn ${section === 'improvements' ? 'active' : ''}`}
            onClick={() => setSection('improvements')}
            type="button"
            id="toggle-improvements"
          >
            <span className="section-toggle-icon">🚀</span>
            Improvements
            {totalImprovements > 0 && (
              <span className="section-badge">{totalImprovements}</span>
            )}
          </button>
        </div>
      </div>

      {/* ── RESUME DETAILS SECTION ──────────────────── */}
      <div className={`section-panel ${section === 'resume' ? 'section-panel-active' : ''}`}>
        {/* Match Score */}
        <div className="card">
          <div className="card-title">
            <span className="icon">📊</span> Skill Match
          </div>
          <div className="match-section">
            <MatchRing percentage={match.percentage} />
            <div className="match-details">
              <h3>{match.percentage}% Match</h3>
              <p>
                {match.found.length} of {match.found.length + match.missing.length} required skills found
              </p>
            </div>
          </div>
          <div className="tag-list">
            {match.found.map((s) => (
              <span key={s} className="tag tag-found">{s}</span>
            ))}
            {match.missing.map((s) => (
              <span key={s} className="tag tag-missing">{s}</span>
            ))}
          </div>
        </div>

        {/* Personal Info */}
        <div className="card">
          <div className="card-title">
            <span className="icon">👤</span> Personal Information
          </div>
          <div className="info-grid">
            {parsed.name && (
              <div className="info-item">
                <div className="info-label">Name</div>
                <div className="info-value">{parsed.name}</div>
              </div>
            )}
            {parsed.email && (
              <div className="info-item">
                <div className="info-label">Email</div>
                <div className="info-value">{parsed.email}</div>
              </div>
            )}
            {parsed.phone && (
              <div className="info-item">
                <div className="info-label">Phone</div>
                <div className="info-value">{parsed.phone}</div>
              </div>
            )}
            {parsed.skills?.length > 0 && (
              <div className="info-item">
                <div className="info-label">Skills Found</div>
                <div className="info-value">{parsed.skills.length}</div>
              </div>
            )}
            {parsed.linkedin && (
              <div className="info-item">
                <div className="info-label">LinkedIn</div>
                <div className="info-value">
                  <a href={parsed.linkedin} target="_blank" rel="noopener noreferrer" className="info-link">
                    🔗 {parsed.linkedin.replace(/https?:\/\/(www\.)?/, '')}
                  </a>
                </div>
              </div>
            )}
            {parsed.github && (
              <div className="info-item">
                <div className="info-label">GitHub</div>
                <div className="info-value">
                  <a href={parsed.github} target="_blank" rel="noopener noreferrer" className="info-link">
                    🔗 {parsed.github.replace(/https?:\/\/(www\.)?/, '')}
                  </a>
                </div>
              </div>
            )}
          </div>

          {/* All Skills Tags */}
          {parsed.all_skills?.length > 0 && (
            <div className="all-skills-section">
              <div className="info-label" style={{ marginBottom: 8, marginTop: 16 }}>All Skills</div>
              <div className="tag-list">
                {parsed.all_skills.map((s, i) => (
                  <span key={i} className="tag tag-skill">{s}</span>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Education */}
        {parsed.education?.length > 0 && (
          <div className="card">
            <div className="card-title">
              <span className="icon">🎓</span> Education
            </div>
            <ul className="section-list">
              {parsed.education.map((item, i) => (
                <li key={i} className="edu-item">
                  {typeof item === 'string' ? (
                    item
                  ) : (
                    <>
                      {item.degree && <div className="edu-degree">{item.degree}</div>}
                      {item.institution && <div className="edu-institution">{item.institution}</div>}
                      {item.year && <div className="edu-year">{item.year}</div>}
                    </>
                  )}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Experience */}
        {parsed.experience?.length > 0 && (
          <div className="card">
            <div className="card-title">
              <span className="icon">💼</span> Experience
            </div>
            <ul className="section-list">
              {parsed.experience.map((item, i) => (
                <li key={i} className="exp-item">
                  {typeof item === 'string' ? (
                    item
                  ) : (
                    <>
                      <div className="exp-header">
                        {item.title && <span className="exp-title">{item.title}</span>}
                        {item.company && <span className="exp-company"> · {item.company}</span>}
                      </div>
                      {item.duration && <div className="exp-duration">{item.duration}</div>}
                      {item.description && <div className="exp-desc">{item.description}</div>}
                    </>
                  )}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Projects */}
        {parsed.projects?.length > 0 && (
          <div className="card">
            <div className="card-title">
              <span className="icon">🛠️</span> Projects
            </div>
            <ul className="section-list">
              {parsed.projects.map((p, i) => (
                <li key={i} className="project-item">
                  <strong>{p.title || 'Untitled'}</strong>
                  {p.description && <div className="project-desc">{p.description}</div>}
                  {p.technologies?.length > 0 && (
                    <div className="tech-list" style={{ marginTop: 6 }}>
                      {p.technologies.map((t, j) => (
                        <span key={j} className="tech-tag">{t}</span>
                      ))}
                    </div>
                  )}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Certifications */}
        {parsed.certifications?.length > 0 && (
          <div className="card">
            <div className="card-title">
              <span className="icon">🏅</span> Certifications
            </div>
            <ul className="section-list">
              {parsed.certifications.map((c, i) => (
                <li key={i}>{typeof c === 'string' ? c : (c.name || c.title || formatEducation(c))}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* ── IMPROVEMENTS SECTION ────────────────────── */}
      <div className={`section-panel ${section === 'improvements' ? 'section-panel-active' : ''}`}>
        {qa && !qa.error ? (
          <>
            {/* Sub-tabs for improvement categories */}
            <div className="card">
              <div className="card-title">
                <span className="icon">🤖</span> AI-Powered Insights
              </div>

              <div className="tabs">
                <button
                  className={`tab-btn ${tab === 'overview' ? 'active' : ''}`}
                  onClick={() => setTab('overview')}
                  type="button"
                  id="tab-missing-skills"
                >
                  Missing Skills
                  {missingCount > 0 && <span className="tab-count">{missingCount}</span>}
                </button>
                <button
                  className={`tab-btn ${tab === 'projects' ? 'active' : ''}`}
                  onClick={() => setTab('projects')}
                  type="button"
                  id="tab-projects"
                >
                  Project Ideas
                  {projectCount > 0 && <span className="tab-count">{projectCount}</span>}
                </button>
                <button
                  className={`tab-btn ${tab === 'interview' ? 'active' : ''}`}
                  onClick={() => setTab('interview')}
                  type="button"
                  id="tab-interview"
                >
                  Interview Q&A
                  {interviewCount > 0 && <span className="tab-count">{interviewCount}</span>}
                </button>
              </div>

              <div className="tab-content">
                {tab === 'overview' && (
                  <div className="tab-panel-animate">
                    {qa.missing_skills?.map((item, i) => (
                      <div key={i} className="missing-skill-item">
                        <span className={`priority-badge priority-${item.priority || 'low'}`}>
                          {item.priority || 'low'}
                        </span>
                        <div className="missing-skill-info">
                          <div className="skill-name">{item.skill}</div>
                          <div className="skill-reason">{item.reason}</div>
                        </div>
                      </div>
                    ))}
                    {(!qa.missing_skills || qa.missing_skills.length === 0) && (
                      <div className="empty-state">
                        <span className="empty-state-icon">🎉</span>
                        <p>No missing skills identified. Great job!</p>
                      </div>
                    )}
                  </div>
                )}

                {tab === 'projects' && (
                  <div className="tab-panel-animate">
                    {qa.project_suggestions?.map((p, i) => (
                      <div key={i} className="project-card">
                        <span className="diff-badge">{p.difficulty}</span>
                        <h4>{p.title}</h4>
                        <p>{p.description}</p>
                        {p.skills_targeted?.length > 0 && (
                          <div className="tech-list">
                            {p.skills_targeted.map((s, j) => (
                              <span key={j} className="tech-tag">{s}</span>
                            ))}
                          </div>
                        )}
                      </div>
                    ))}
                    {(!qa.project_suggestions || qa.project_suggestions.length === 0) && (
                      <div className="empty-state">
                        <span className="empty-state-icon">📦</span>
                        <p>No project suggestions available.</p>
                      </div>
                    )}
                  </div>
                )}

                {tab === 'interview' && (
                  <div className="tab-panel-animate">
                    <InterviewQA items={qa.interview_QA || []} />
                  </div>
                )}
              </div>
            </div>

            {/* Quick Summary Card */}
            <div className="card improvement-summary-card">
              <div className="card-title">
                <span className="icon">📋</span> Quick Summary
              </div>
              <div className="summary-stats">
                <div className="summary-stat">
                  <div className="summary-stat-number">{missingCount}</div>
                  <div className="summary-stat-label">Skills to Learn</div>
                </div>
                <div className="summary-stat-divider" />
                <div className="summary-stat">
                  <div className="summary-stat-number">{projectCount}</div>
                  <div className="summary-stat-label">Project Ideas</div>
                </div>
                <div className="summary-stat-divider" />
                <div className="summary-stat">
                  <div className="summary-stat-number">{interviewCount}</div>
                  <div className="summary-stat-label">Practice Questions</div>
                </div>
              </div>
            </div>
          </>
        ) : (
          <div className="card">
            <div className="empty-state">
              <span className="empty-state-icon">🔍</span>
              <p>No improvement data available.</p>
            </div>
          </div>
        )}
      </div>

      {/* ── Actions ─────────────────────────────────── */}
      <div style={{ display: 'flex', gap: '10px', justifyContent: 'center', marginTop: 20 }}>
        <button className="btn btn-primary" onClick={downloadReport} style={{ width: 'auto', flex: 1 }}>
          📥 Download Report
        </button>
        <button className="btn btn-ghost" onClick={onReset} id="reset-btn" style={{ width: 'auto', flex: 1 }}>
          ← Analyse Another Resume
        </button>
      </div>
    </>
  )
}

function InterviewQA({ items }) {
  const [openIdx, setOpenIdx] = useState(null)

  // Group by category
  const grouped = {}
  items.forEach((item) => {
    const cat = item.category || 'general'
    if (!grouped[cat]) grouped[cat] = []
    grouped[cat].push(item)
  })

  if (items.length === 0) {
    return (
      <div className="empty-state">
        <span className="empty-state-icon">💬</span>
        <p>No interview questions available.</p>
      </div>
    )
  }

  return (
    <div>
      {Object.entries(grouped).map(([category, questions]) => (
        <div key={category} className="qa-category">
          <h3>{category}</h3>
          {questions.map((q, i) => {
            const globalIdx = `${category}-${i}`
            const isOpen = openIdx === globalIdx
            return (
              <div key={i} className="qa-item">
                <button
                  className="qa-question"
                  onClick={() => setOpenIdx(isOpen ? null : globalIdx)}
                  type="button"
                >
                  <span>{q.question}</span>
                  <span className={`qa-chevron ${isOpen ? 'open' : ''}`}>▼</span>
                </button>
                {isOpen && <div className="qa-answer">{q.answer}</div>}
              </div>
            )
          })}
        </div>
      ))}
    </div>
  )
}
