#!/usr/bin/env node
/**
 * Mobile Responsiveness Validation Script
 * 
 * This script validates the interactive.html file for mobile responsiveness
 * Run with: node validate-mobile.js
 */

const fs = require('fs');
const path = require('path');

const INTERACTIVE_HTML = path.join(__dirname, 'interactive.html');

let errors = [];
let warnings = [];
let passes = [];

function checkViewport() {
  const content = fs.readFileSync(INTERACTIVE_HTML, 'utf8');
  const hasViewport = content.includes('<meta name="viewport"');
  const hasWidthDeviceWidth = content.includes('width=device-width');
  const hasInitialScale = content.includes('initial-scale=1');
  
  if (hasViewport && hasWidthDeviceWidth && hasInitialScale) {
    passes.push('✓ Viewport meta tag is correctly configured');
  } else {
    errors.push('✗ Viewport meta tag is missing or incorrect');
  }
}

function checkResponsiveCSS() {
  const content = fs.readFileSync(INTERACTIVE_HTML, 'utf8');
  const hasMedia840 = content.includes('@media (max-width: 840px)');
  const hasMedia480 = content.includes('@media (max-width: 480px)');
  const hasMinHeight = content.includes('min-height: 500px') || content.includes('min-height:450px');
  const hasMaxHeight = content.includes('max-height: 80vh') || content.includes('max-height:75vh');
  
  if (hasMedia840 && hasMedia480) {
    passes.push('✓ Media queries for breakpoints are present');
  } else {
    errors.push('✗ Missing required media query breakpoints');
  }
  
  if (hasMinHeight && hasMaxHeight) {
    passes.push('✓ Responsive height constraints are set');
  } else {
    warnings.push('⚠ Responsive height constraints may be incomplete');
  }
}

function checkJavaScript() {
  const content = fs.readFileSync(INTERACTIVE_HTML, 'utf8');
  const hasResizeFunction = content.includes('function resizeChart') || content.includes('resizeChart()');
  const hasResizeListener = content.includes('addEventListener(\'resize\'') || content.includes('addEventListener("resize"');
  const hasOrientationListener = content.includes('orientationchange');
  const hasVisualViewport = content.includes('visualViewport');
  const hasMatchMedia = content.includes('matchMedia');
  
  if (hasResizeFunction) {
    passes.push('✓ resizeChart function is defined');
  } else {
    errors.push('✗ resizeChart function is missing');
  }
  
  if (hasResizeListener) {
    passes.push('✓ Window resize listener is attached');
  } else {
    errors.push('✗ Window resize listener is missing');
  }
  
  if (hasOrientationListener) {
    passes.push('✓ Orientation change listener is attached');
  } else {
    errors.push('✗ Orientation change listener is missing');
  }
  
  if (hasVisualViewport) {
    passes.push('✓ Visual viewport API is used (modern browsers)');
  } else {
    warnings.push('⚠ Visual viewport API not used (may affect mobile browsers with dynamic UI)');
  }
  
  if (hasMatchMedia) {
    passes.push('✓ MatchMedia API is used for breakpoint detection');
  } else {
    warnings.push('⚠ MatchMedia API not used (may affect breakpoint detection)');
  }
}

function checkIframe() {
  const content = fs.readFileSync(INTERACTIVE_HTML, 'utf8');
  const hasIframe = content.includes('<iframe');
  const hasLoading = content.includes('loading="lazy"') || content.includes('loading=\'lazy\'');
  const hasTitle = content.includes('title="Interactive Dataset Explorer"');
  
  if (hasIframe) {
    passes.push('✓ Iframe element is present');
  } else {
    errors.push('✗ Iframe element is missing');
  }
  
  if (hasLoading) {
    passes.push('✓ Iframe has lazy loading attribute');
  } else {
    warnings.push('⚠ Iframe missing lazy loading attribute');
  }
  
  if (hasTitle) {
    passes.push('✓ Iframe has accessibility title');
  } else {
    warnings.push('⚠ Iframe missing accessibility title');
  }
}

function checkTouchSupport() {
  const content = fs.readFileSync(INTERACTIVE_HTML, 'utf8');
  const hasTouchAction = content.includes('touch-action');
  const hasWebkitOverflow = content.includes('-webkit-overflow-scrolling');
  
  if (hasTouchAction) {
    passes.push('✓ Touch action CSS is configured');
  } else {
    warnings.push('⚠ Touch action CSS not configured');
  }
  
  if (hasWebkitOverflow) {
    passes.push('✓ WebKit overflow scrolling is enabled');
  } else {
    warnings.push('⚠ WebKit overflow scrolling not enabled');
  }
}

// Run all checks
console.log('🔍 Validating mobile responsiveness...\n');

try {
  checkViewport();
  checkResponsiveCSS();
  checkJavaScript();
  checkIframe();
  checkTouchSupport();
  
  // Print results
  console.log('\n📊 Validation Results:\n');
  
  if (passes.length > 0) {
    console.log('✅ PASSED CHECKS:');
    passes.forEach(p => console.log(`  ${p}`));
    console.log('');
  }
  
  if (warnings.length > 0) {
    console.log('⚠️  WARNINGS:');
    warnings.forEach(w => console.log(`  ${w}`));
    console.log('');
  }
  
  if (errors.length > 0) {
    console.log('❌ ERRORS:');
    errors.forEach(e => console.log(`  ${e}`));
    console.log('');
  }
  
  // Summary
  const total = passes.length + warnings.length + errors.length;
  console.log(`\n📈 Summary: ${passes.length} passed, ${warnings.length} warnings, ${errors.length} errors\n`);
  
  if (errors.length === 0) {
    console.log('✅ All critical checks passed! The page should work well on mobile devices.');
    console.log('💡 Review warnings for potential improvements.');
    process.exit(0);
  } else {
    console.log('❌ Some critical checks failed. Please fix errors before deploying.');
    process.exit(1);
  }
  
} catch (error) {
  console.error('❌ Error reading interactive.html:', error.message);
  process.exit(1);
}

