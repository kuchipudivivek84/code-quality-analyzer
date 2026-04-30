import streamlit as st
from analyzer import analyze_code

st.set_page_config(page_title="Code Quality Analyzer")

st.title("💻 Code Quality Analyzer")

st.write("Paste your Python code below:")

code = st.text_area("Your Code Here", height=250)

if st.button("Analyze Code"):
    if code.strip() != "":
        score, issues, complexity = analyze_code(code)

        st.subheader("📊 Results")
        
        # Color-based score
        if score >= 8:
            st.success(f"Quality Score: {score} / 10")
        elif score >= 5:
            st.warning(f"Quality Score: {score} / 10")
        else:
            st.error(f"Quality Score: {score} / 10")

        st.subheader("⚠️ Issues Found")
        if issues:
            for issue in issues:
                st.write("-", issue)
        else:
            st.write("✅ No major issues found")

        st.subheader("🔢 Complexity")
        st.write(complexity)

    else:
        st.warning("Please enter some code!")