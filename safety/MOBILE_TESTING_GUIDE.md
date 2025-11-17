# Mobile Testing Guide for Interactive Chart

This guide provides comprehensive instructions for testing the mobile responsiveness of the interactive chart page.

## Quick Test Checklist

### ✅ Pre-Testing Setup
- [ ] Open `interactive.html` in a browser
- [ ] Open browser developer tools (F12)
- [ ] Enable device emulation mode
- [ ] Test with `test-mobile.html` validation page

### 📱 Device Breakpoints to Test

1. **Small Mobile (< 480px)**
   - iPhone SE (375px)
   - Small Android phones (360px)
   - Expected: Chart uses 75vh max-height, min 450px

2. **Mobile (480px - 840px)**
   - iPhone 12/13/14 (390px)
   - iPhone 12/13/14 Pro Max (428px)
   - Pixel 5 (393px)
   - Expected: Chart uses 80vh max-height, min 500px

3. **Desktop (> 840px)**
   - iPad (768px)
   - Desktop (1024px+)
   - Expected: Chart uses 65vh or fixed 600-750px

## Browser Testing

### Chrome DevTools
1. Open Chrome DevTools (F12)
2. Click device toolbar icon (Ctrl+Shift+M)
3. Test these presets:
   - iPhone SE
   - iPhone 12 Pro
   - Pixel 5
   - iPad
   - Custom sizes: 360px, 480px, 840px

### Firefox Responsive Design Mode
1. Open Firefox DevTools (F12)
2. Click responsive design mode (Ctrl+Shift+M)
3. Test same device presets as Chrome

### Safari (macOS)
1. Enable Develop menu: Preferences > Advanced > Show Develop menu
2. Develop > Enter Responsive Design Mode
3. Test iOS device presets

## Physical Device Testing

### iOS Devices
- **iPhone SE (1st/2nd gen)**: 375px width
- **iPhone 12/13/14**: 390px width
- **iPhone 12/13/14 Pro Max**: 428px width
- **iPad**: 768px width (portrait)

**Test Steps:**
1. Open `interactive.html` in Safari
2. Rotate device to test orientation changes
3. Verify chart resizes smoothly
4. Check that chart doesn't overflow viewport
5. Test touch interactions (if applicable)

### Android Devices
- **Small phones**: 360px width
- **Standard phones**: 393px width
- **Large phones**: 428px width
- **Tablets**: 768px+ width

**Test Steps:**
1. Open `interactive.html` in Chrome
2. Rotate device to test orientation changes
3. Verify chart resizes smoothly
4. Check that chart doesn't overflow viewport
5. Test touch interactions

## Automated Testing with test-mobile.html

1. Open `test-mobile.html` in your browser
2. The page will automatically run tests on load
3. Review test results:
   - ✅ **PASS**: Feature works correctly
   - ⚠️ **WARNING**: May work but needs verification
   - ❌ **FAIL**: Feature is missing or broken

## Key Features to Verify

### 1. Chart Container Sizing
- [ ] Chart adapts to screen width
- [ ] Chart height is appropriate for viewport
- [ ] No horizontal scrolling
- [ ] Chart doesn't overflow container

### 2. Responsive Breakpoints
- [ ] Styles change at 840px breakpoint
- [ ] Styles change at 480px breakpoint
- [ ] Smooth transitions between breakpoints

### 3. JavaScript Functionality
- [ ] `resizeChart()` function executes on load
- [ ] Window resize triggers chart resize
- [ ] Orientation change triggers chart resize
- [ ] Debouncing prevents excessive resize calls

### 4. Touch Interactions
- [ ] Chart is scrollable/zoomable (if Plotly supports)
- [ ] No touch event conflicts
- [ ] Smooth scrolling on mobile

### 5. Performance
- [ ] Chart loads within 3 seconds on 3G
- [ ] Resize operations are smooth (no jank)
- [ ] No memory leaks during resize

## Common Issues & Solutions

### Issue: Chart doesn't resize on mobile
**Solution**: Check browser console for JavaScript errors. Verify `resizeChart()` function is defined and called.

### Issue: Chart overflows viewport
**Solution**: Verify CSS `max-height` is set correctly. Check that `overflow: hidden` is on container.

### Issue: Chart doesn't resize on orientation change
**Solution**: Verify `orientationchange` event listener is attached. Check for timing issues (may need longer delay).

### Issue: Chart is too small on mobile
**Solution**: Adjust `min-height` values in CSS. Verify viewport meta tag is correct.

### Issue: Chart doesn't load
**Solution**: Check iframe `src` path is correct. Verify CORS settings if loading from different domain.

## Testing Tools

### Online Tools
- **BrowserStack**: https://www.browserstack.com (free trial)
- **LambdaTest**: https://www.lambdatest.com (free trial)
- **Responsive Design Checker**: https://responsivedesignchecker.com

### Browser Extensions
- **Window Resizer** (Chrome): Resize browser to specific dimensions
- **Responsive Viewer** (Chrome): View multiple breakpoints simultaneously

## Expected Behavior Summary

| Screen Size | Chart Height | Notes |
|------------|--------------|-------|
| < 480px | 75vh (min 450px) | Small mobile devices |
| 480px - 840px | 80vh (min 500px) | Standard mobile devices |
| > 840px | 65vh (600-750px) | Tablets and desktop |

## Reporting Issues

When reporting mobile issues, include:
1. Device model and OS version
2. Browser and version
3. Screen dimensions
4. Steps to reproduce
5. Screenshots or screen recordings
6. Browser console errors (if any)

## Continuous Testing

For ongoing testing:
1. Run `test-mobile.html` after each code change
2. Test on at least one iOS and one Android device
3. Verify in Chrome DevTools for common breakpoints
4. Check orientation changes work correctly

