/*
  Warnings:

  - You are about to drop the column `submissionId` on the `File` table. All the data in the column will be lost.
  - Added the required column `userId` to the `File` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "File" DROP CONSTRAINT "File_submissionId_fkey";

-- AlterTable
ALTER TABLE "File" DROP COLUMN "submissionId",
ADD COLUMN     "userId" TEXT NOT NULL;

-- AddForeignKey
ALTER TABLE "File" ADD CONSTRAINT "File_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
