/*
  Warnings:

  - You are about to drop the column `courseworkId` on the `Submission` table. All the data in the column will be lost.
  - You are about to drop the `Coursework` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `CoursworkId` to the `Submission` table without a default value. This is not possible if the table is not empty.

*/
-- CreateEnum
CREATE TYPE "CoursworkType" AS ENUM ('Assignment', 'Quiz', 'Project', 'Exam', 'Other');

-- DropForeignKey
ALTER TABLE "Coursework" DROP CONSTRAINT "Coursework_classroomId_fkey";

-- DropForeignKey
ALTER TABLE "Coursework" DROP CONSTRAINT "Coursework_professorId_fkey";

-- DropForeignKey
ALTER TABLE "Submission" DROP CONSTRAINT "Submission_courseworkId_fkey";

-- AlterTable
ALTER TABLE "Submission" DROP COLUMN "courseworkId",
ADD COLUMN     "CoursworkId" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "image" TEXT;

-- DropTable
DROP TABLE "Coursework";

-- CreateTable
CREATE TABLE "Courswork" (
    "id" TEXT NOT NULL,
    "classroomId" TEXT NOT NULL,
    "professorId" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "type" "CoursworkType" NOT NULL,
    "description" TEXT NOT NULL,
    "due_date" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Courswork_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Courswork" ADD CONSTRAINT "Courswork_classroomId_fkey" FOREIGN KEY ("classroomId") REFERENCES "Classroom"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Courswork" ADD CONSTRAINT "Courswork_professorId_fkey" FOREIGN KEY ("professorId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Submission" ADD CONSTRAINT "Submission_CoursworkId_fkey" FOREIGN KEY ("CoursworkId") REFERENCES "Courswork"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
