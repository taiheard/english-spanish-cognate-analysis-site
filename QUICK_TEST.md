# Quick Mobile Testing Instructions

## Automated Testing

### Option 1: Run Validation Script
```bash
node validate-mobile.js
```
This will check all code for mobile responsiveness requirements.

### Option 2: Use Test Page
1. Open `test-mobile.html` in your browser
2. Tests run automatically on page load
3. Review results for any issues

## Manual Browser Testing

### Chrome DevTools (Recommended)
1. Open `interactive.html` in Chrome
2. Press `F12` to open DevTools
3. Press `Ctrl+Shift+M` (or click device icon) to enable device mode
4. Test these devices:
   - **iPhone SE** (375px) - Small mobile
   - **iPhone 12 Pro** (390px) - Standard mobile
   - **Pixel 5** (393px) - Android mobile
   - **iPad** (768px) - Tablet
5. Rotate device to test orientation changes
6. Resize window to test smooth transitions

### Firefox Responsive Design Mode
1. Open `interactive.html` in Firefox
2. Press `F12` to open DevTools
3. Press `Ctrl+Shift+M` for responsive design mode
4. Test same devices as Chrome

## What to Check

✅ **Chart Container**
- Chart fits within viewport
- No horizontal scrolling
- Height adapts to screen size

✅ **Responsive Breakpoints**
- Styles change at 840px (mobile menu appears)
- Styles change at 480px (smaller chart height)

✅ **JavaScript Functionality**
- Chart resizes on window resize
- Chart resizes on orientation change
- Smooth transitions (no jank)

✅ **Touch Interactions**
- Chart is scrollable/zoomable
- No touch conflicts

## Expected Behavior

| Screen Width | Chart Height | Notes |
|-------------|--------------|-------|
| < 480px | 75vh (min 450px) | Very small phones |
| 480-840px | 80vh (min 500px) | Standard phones |
| > 840px | 65vh (600-750px) | Tablets/Desktop |

## Common Issues

**Chart doesn't resize?**
- Check browser console for errors
- Verify JavaScript is enabled
- Try hard refresh (Ctrl+Shift+R)

**Chart overflows?**
- Check CSS max-height is set
- Verify container has overflow: hidden

**Orientation change doesn't work?**
- Wait 1-2 seconds after rotation
- Check orientationchange event is firing

## Testing Checklist

- [ ] Test on Chrome DevTools (mobile emulation)
- [ ] Test on Firefox Responsive Design Mode
- [ ] Test on actual iOS device (if available)
- [ ] Test on actual Android device (if available)
- [ ] Test orientation changes
- [ ] Test window resizing
- [ ] Verify no console errors
- [ ] Verify chart loads and displays correctly
- [ ] Verify chart is interactive (hover/click works)

## Need Help?

See `MOBILE_TESTING_GUIDE.md` for comprehensive testing instructions.

