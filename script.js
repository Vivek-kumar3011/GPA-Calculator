function showSection(sectionId) {
  document.querySelectorAll(".section").forEach(sec => sec.style.display = "none");
  document.getElementById(sectionId).style.display = "block";
}

function clearAll() {
  location.reload();
}

// SGPA Logic
let subjectCount = 0;
function addSubject() {
  subjectCount++;
  const container = document.getElementById("sgpaInputs");
  const div = document.createElement("div");
  div.innerHTML = `
    Subject ${subjectCount}:
    <select>
      <option value="10">EX/S/A+</option>
      <option value="9">A</option>
      <option value="8">B</option>
      <option value="7">C</option>
      <option value="6">D</option>
      <option value="5">P</option>
      <option value="4">E</option>
      <option value="0">F/FR</option>
      <option value="skip">U</option>
    </select>
    Credit: <input type="number" min="1" />
  `;
  container.appendChild(div);
}

function calculateSGPA() {
  const inputs = document.querySelectorAll("#sgpaInputs div");
  let totalPoints = 0, totalCredits = 0;

  inputs.forEach(div => {
    const grade = div.querySelector("select").value;
    const credit = parseInt(div.querySelector("input").value);

    if (grade !== "skip") {
      totalPoints += parseInt(grade) * credit;
      totalCredits += credit;
    }
  });

  const sgpa = (totalCredits > 0) ? (totalPoints / totalCredits).toFixed(2) : "Invalid Input";
  document.getElementById("sgpaResult").innerText = `Your SGPA is: ${sgpa}`;
}

// CGPA Logic
function generateSemInputs() {
  const semCount = parseInt(document.getElementById("semesters").value);
  const container = document.getElementById("cgpaInputs");
  container.innerHTML = "";

  for (let i = 1; i <= semCount; i++) {
    const div = document.createElement("div");
    div.innerHTML = `
      Semester ${i}: SGPA <input type="number" step="0.01" min="0" max="10" /> 
      Credits <input type="number" min="1" />
    `;
    container.appendChild(div);
  }
}

function calculateCGPA() {
  const inputs = document.querySelectorAll("#cgpaInputs div");
  let totalPoints = 0, totalCredits = 0;

  inputs.forEach(div => {
    const sgpa = parseFloat(div.querySelectorAll("input")[0].value);
    const credit = parseInt(div.querySelectorAll("input")[1].value);

    if (!isNaN(sgpa) && !isNaN(credit)) {
      totalPoints += sgpa * credit;
      totalCredits += credit;
    }
  });

  const cgpa = (totalCredits > 0) ? (totalPoints / totalCredits).toFixed(2) : "Invalid Input";
  document.getElementById("cgpaResult").innerText = `Your CGPA is: ${cgpa}`;
}

// Target CGPA Logic
function calculateTargetSGPA() {
  const currentCgpa = parseFloat(document.getElementById("currentCgpa").value);
  const currentCredits = parseInt(document.getElementById("currentCredits").value);
  const targetCgpa = parseFloat(document.getElementById("targetCgpa").value);
  const upcomingCredits = parseInt(document.getElementById("upcomingCredits").value);

  const neededTotal = targetCgpa * (currentCredits + upcomingCredits);
  const currentTotal = currentCgpa * currentCredits;
  const neededPoints = neededTotal - currentTotal;
  const requiredSgpa = neededPoints / upcomingCredits;

  let message = "";
  if (requiredSgpa > 10) {
    message = "Required SGPA is more than 10. Not achievable.";
  } else if (requiredSgpa < 0) {
    message = "Target already achieved!";
  } else {
    message = `You need an SGPA of ${requiredSgpa.toFixed(2)} in your next semester.`;
  }

  document.getElementById("targetResult").innerText = message;
}