-- CreateEnum
CREATE TYPE "Gender" AS ENUM ('Male', 'Female');

-- CreateEnum
CREATE TYPE "UserRole" AS ENUM ('Student', 'Professeur');

-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "gender" "Gender" NOT NULL,
    "role" "UserRole" NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Classroom" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "professorId" TEXT NOT NULL,

    CONSTRAINT "Classroom_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Enrollment" (
    "id" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    "classroomId" TEXT NOT NULL,

    CONSTRAINT "Enrollment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Coursework" (
    "id" TEXT NOT NULL,
    "classroomId" TEXT NOT NULL,
    "professorId" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "Assignment" BOOLEAN NOT NULL,
    "description" TEXT NOT NULL,
    "due_date" TEXT NOT NULL,

    CONSTRAINT "Coursework_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Submission" (
    "id" TEXT NOT NULL,
    "courseworkId" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    "content" TEXT NOT NULL,

    CONSTRAINT "Submission_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "_StudentClassrooms" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "_StudentClassrooms_AB_unique" ON "_StudentClassrooms"("A", "B");

-- CreateIndex
CREATE INDEX "_StudentClassrooms_B_index" ON "_StudentClassrooms"("B");

-- AddForeignKey
ALTER TABLE "Classroom" ADD CONSTRAINT "Classroom_professorId_fkey" FOREIGN KEY ("professorId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Enrollment" ADD CONSTRAINT "Enrollment_studentId_fkey" FOREIGN KEY ("studentId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Enrollment" ADD CONSTRAINT "Enrollment_classroomId_fkey" FOREIGN KEY ("classroomId") REFERENCES "Classroom"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Coursework" ADD CONSTRAINT "Coursework_classroomId_fkey" FOREIGN KEY ("classroomId") REFERENCES "Classroom"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Coursework" ADD CONSTRAINT "Coursework_professorId_fkey" FOREIGN KEY ("professorId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Submission" ADD CONSTRAINT "Submission_courseworkId_fkey" FOREIGN KEY ("courseworkId") REFERENCES "Coursework"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Submission" ADD CONSTRAINT "Submission_studentId_fkey" FOREIGN KEY ("studentId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_StudentClassrooms" ADD CONSTRAINT "_StudentClassrooms_A_fkey" FOREIGN KEY ("A") REFERENCES "Classroom"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_StudentClassrooms" ADD CONSTRAINT "_StudentClassrooms_B_fkey" FOREIGN KEY ("B") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
