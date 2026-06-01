export default function MatchRing({ percentage }) {
  const radius = 42
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (percentage / 100) * circumference

  return (
    <div className="match-ring">
      <svg width="100" height="100" viewBox="0 0 100 100">
        <circle className="ring-bg" cx="50" cy="50" r={radius} />
        <circle
          className="ring-fill"
          cx="50"
          cy="50"
          r={radius}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
        />
      </svg>
      <div className="ring-label">{Math.round(percentage)}%</div>
    </div>
  )
}
