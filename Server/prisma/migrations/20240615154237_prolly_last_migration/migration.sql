/*
  Warnings:

  - You are about to drop the `_StudentClassrooms` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "_StudentClassrooms" DROP CONSTRAINT "_StudentClassrooms_A_fkey";

-- DropForeignKey
ALTER TABLE "_StudentClassrooms" DROP CONSTRAINT "_StudentClassrooms_B_fkey";

-- DropTable
DROP TABLE "_StudentClassrooms";

-- CreateTable
CREATE TABLE "File" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "path" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "size" TEXT NOT NULL,
    "submissionId" TEXT NOT NULL,

    CONSTRAINT "File_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "File" ADD CONSTRAINT "File_submissionId_fkey" FOREIGN KEY ("submissionId") REFERENCES "Submission"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
