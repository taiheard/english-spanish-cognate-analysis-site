// Dataset Explorer - Chart.js implementation
// Loads CSV data and displays all datapoints in a scatter plot

(function() {
  'use strict';

  const CSV_PATH = 'language_analysis_masterframe25OCT.csv';
  let chart = null;
  let allData = [];

  // Color mapping for relationship types
  const relationshipColors = {
    'cognates': 'rgba(10, 61, 98, 0.6)',
    'false_friends': 'rgba(255, 107, 53, 0.7)',
    'loanword_en_to_es': 'rgba(76, 175, 80, 0.6)',
    'loanword_es_to_en': 'rgba(156, 39, 176, 0.6)'
  };

  // Parse CSV data
  function parseCSV(csvText) {
    const parsed = Papa.parse(csvText, {
      header: true,
      skipEmptyLines: true,
      dynamicTyping: true
    });
    return parsed.data.filter(row => 
      row.levenshtein_similarity != null && 
      row.complexity_overall_complexity != null &&
      !isNaN(row.levenshtein_similarity) &&
      !isNaN(row.complexity_overall_complexity)
    );
  }

  // Group data by relationship type
  function groupDataByRelationship(data) {
    const grouped = {};
    data.forEach(row => {
      const type = row.relationship_type || 'unknown';
      if (!grouped[type]) {
        grouped[type] = {
          label: type.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
          data: [],
          backgroundColor: relationshipColors[type] || 'rgba(128, 128, 128, 0.6)',
          borderColor: relationshipColors[type] || 'rgba(128, 128, 128, 0.8)',
          pointRadius: 3,
          pointHoverRadius: 5
        };
      }
      grouped[type].data.push({
        x: row.levenshtein_similarity,
        y: row.complexity_overall_complexity,
        english_word: row.english_word,
        spanish_word: row.spanish_word,
        relationship_type: row.relationship_type,
        cultural_domain: row.cultural_domain
      });
    });
    return Object.values(grouped);
  }

  // Create Chart.js scatter plot
  function createChart(datasets) {
    const ctx = document.getElementById('datasetChart');
    if (!ctx) return;

    const container = document.getElementById('chart-container');
    if (!container) return;

    // Calculate available space
    const containerRect = container.getBoundingClientRect();
    const padding = 60; // Account for container padding
    const availableHeight = containerRect.height - padding;
    const availableWidth = containerRect.width - padding;

    // Destroy existing chart if present
    if (chart) {
      chart.destroy();
    }

    // Set canvas dimensions explicitly
    ctx.width = availableWidth;
    ctx.height = availableHeight;

    chart = new Chart(ctx, {
      type: 'scatter',
      data: {
        datasets: datasets
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        layout: {
          padding: {
            top: 10,
            right: 10,
            bottom: 10,
            left: 10
          }
        },
        plugins: {
          legend: {
            display: true,
            position: 'top',
            labels: {
              usePointStyle: true,
              padding: 12,
              font: {
                size: 11
              },
              boxWidth: 12,
              boxHeight: 12
            }
          },
          tooltip: {
            callbacks: {
              title: function(context) {
                return '';
              },
              label: function(context) {
                const point = context.raw;
                return [
                  `English: ${point.english_word}`,
                  `Spanish: ${point.spanish_word}`,
                  `Similarity: ${point.x.toFixed(2)}`,
                  `Complexity: ${point.y.toFixed(2)}`,
                  `Domain: ${point.cultural_domain || 'N/A'}`
                ];
              }
            },
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            padding: 10,
            titleFont: { size: 14, weight: 'bold' },
            bodyFont: { size: 12 },
            displayColors: false
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Levenshtein Similarity',
              font: {
                size: 13,
                weight: 'bold'
              },
              padding: { top: 5, bottom: 5 }
            },
            min: 0,
            max: 1,
            ticks: {
              font: {
                size: 10
              },
              maxTicksLimit: 8
            },
            grid: {
              color: 'rgba(0, 0, 0, 0.05)'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Overall Complexity',
              font: {
                size: 13,
                weight: 'bold'
              },
              padding: { top: 5, bottom: 5 }
            },
            ticks: {
              font: {
                size: 10
              },
              maxTicksLimit: 8
            },
            grid: {
              color: 'rgba(0, 0, 0, 0.05)'
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'point'
        }
      }
    });
  }

  // Load and process data
  function loadData() {
    // Wait for container to be rendered and sized
    function initChart() {
      const container = document.getElementById('chart-container');
      if (!container || container.offsetHeight === 0) {
        // Container not ready, try again
        setTimeout(initChart, 100);
        return;
      }

      fetch(CSV_PATH)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.text();
        })
        .then(csvText => {
          allData = parseCSV(csvText);
          const datasets = groupDataByRelationship(allData);
          // Small delay to ensure container dimensions are stable
          setTimeout(() => {
            createChart(datasets);
          }, 50);
        })
        .catch(error => {
          console.error('Error loading data:', error);
          const container = document.getElementById('chart-container');
          if (container) {
            container.innerHTML = `
              <div style="padding: 2rem; text-align: center; color: var(--text-secondary);">
                <p>Error loading dataset. Please check the CSV file path.</p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">${error.message}</p>
                <p style="font-size: 0.85rem; margin-top: 0.5rem; color: var(--text-muted);">Expected path: ${CSV_PATH}</p>
              </div>
            `;
          }
        });
    }

    initChart();
  }

  // Handle window resize
  let resizeTimeout;
  function handleResize() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function() {
      if (chart && allData.length > 0) {
        const datasets = groupDataByRelationship(allData);
        createChart(datasets);
      }
    }, 250);
  }
  
  window.addEventListener('resize', handleResize);
  
  // Also handle orientation change on mobile
  window.addEventListener('orientationchange', function() {
    setTimeout(handleResize, 500);
  });

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadData);
  } else {
    loadData();
  }
})();

