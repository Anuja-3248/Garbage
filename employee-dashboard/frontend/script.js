async function loadDashboard() {

    try {

        // ==========================================
        // LOAD STATIC DASHBOARD DATA
        // ==========================================

        const response = await fetch("data.json");
        const data = await response.json();

        console.log("Data received from Python:", data);


        // ==========================================
        // SUMMARY CARDS
        // ==========================================

        const totalEmployees =
            data.genders.Male + data.genders.Female;

        document.getElementById("totalEmployees").textContent =
            totalEmployees;

        document.getElementById("maleEmployees").textContent =
            data.genders.Male;

        document.getElementById("femaleEmployees").textContent =
            data.genders.Female;


        // ==========================================
        // AVERAGE SALARY
        // ==========================================

        let totalSalary = 0;
        let employeeCount = 0;

        for (const range in data.salary_ranges) {

            const employees = data.salary_ranges[range];

            employees.forEach(employee => {

                totalSalary += employee.Salary;
                employeeCount++;

            });
        }

        const averageSalary =
            totalSalary / employeeCount;

        document.getElementById("averageSalary").textContent =
            "₹" + Math.round(averageSalary).toLocaleString("en-IN");


        // ==========================================
        // CITY CHART
        // ==========================================

        const cityNames =
            Object.keys(data.cities);

        const cityCounts =
            Object.values(data.cities);


        new Chart(
            document.getElementById("cityChart"),
            {
                type: "bar",

                data: {
                    labels: cityNames,

                    datasets: [{
                        label: "Employees",
                        data: cityCounts
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    plugins: {
                        legend: {
                            display: false
                        }
                    },

                    scales: {
                        y: {
                            beginAtZero: true,

                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                }
            }
        );


        // ==========================================
        // GENDER CHART
        // ==========================================

        const genderNames =
            Object.keys(data.genders);

        const genderCounts =
            Object.values(data.genders);


        new Chart(
            document.getElementById("genderChart"),
            {
                type: "doughnut",

                data: {
                    labels: genderNames,

                    datasets: [{
                        label: "Employees",
                        data: genderCounts
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    plugins: {
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            }
        );


        // ==========================================
        // SALARY DISTRIBUTION CHART
        // ==========================================

        const salaryRanges =
            Object.keys(data.salary_ranges);

        const salaryCounts =
            salaryRanges.map(range =>
                data.salary_ranges[range].length
            );


        new Chart(
            document.getElementById("salaryChart"),
            {
                type: "bar",

                data: {
                    labels: salaryRanges,

                    datasets: [{
                        label: "Employees",
                        data: salaryCounts
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    plugins: {
                        legend: {
                            display: false
                        }
                    },

                    scales: {
                        y: {
                            beginAtZero: true,

                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                }
            }
        );


        // ==========================================
        // EMPLOYEE REPORT
        // ==========================================

        const reportContainer =
            document.getElementById("employeeReportContainer");


        for (const range in data.salary_ranges) {

            const employees =
                data.salary_ranges[range];


            // Create section
            const rangeSection =
                document.createElement("div");

            rangeSection.className =
                "salary-range-section";


            // Salary range heading
            rangeSection.innerHTML = `
                <div class="salary-range-header">

                    <h3>Salary Range: ${range}</h3>

                    <p>
                        Total Employees: ${employees.length}
                    </p>

                </div>
            `;


            // Create table
            const table =
                document.createElement("table");


            table.innerHTML = `
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Post</th>
                        <th>City</th>
                        <th>Gender</th>
                        <th>Salary</th>
                    </tr>
                </thead>

                <tbody></tbody>
            `;


            const tbody =
                table.querySelector("tbody");


            // Add employees
            employees.forEach(employee => {

                const row =
                    document.createElement("tr");


                row.innerHTML = `
                    <td>${employee.ID}</td>
                    <td>${employee.Name}</td>
                    <td>${employee.Post}</td>
                    <td>${employee.City}</td>
                    <td>${employee.Gender}</td>
                    <td>₹${employee.Salary.toLocaleString("en-IN")}</td>
                `;


                tbody.appendChild(row);

            });


            rangeSection.appendChild(table);

            reportContainer.appendChild(rangeSection);

        }
     } catch (error) {

        console.error(
            "Could not connect to Python backend:",
            error
        );

    }

}


loadDashboard();